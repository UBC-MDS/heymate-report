# This script handles computing and uploading popularity scores to SQL Server.
# It combines cleaned menu data with restaurant metrics, calculates a weighted score, and stores the result.
# To use it, run `calculate_and_upload(truncate=True)` to recompute and upload the popularity table.
# Target table: cleaned_menu_with_popularity → used for powering the recommendation system.

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sql_reader import connect_to_sql_server, read_dataframe_from_sql
from sql_uploader import create_table_if_not_exists, truncate_table

def combine_with_metrics(cleaned_table: str = "cleaned_menu_mds") -> pd.DataFrame:
    """
    Join cleaned menu table with restaurant metrics including rating counts and restaurant score.

    Parameters
    ----------
    cleaned_table : str
        The name of the cleaned menu table (default is "cleaned_menu_mds").

    Returns
    -------
    pd.DataFrame
        A joined DataFrame with dish info and restaurant metrics.
    """
    conn, cursor = connect_to_sql_server()

    query = f"""
    SELECT 
    c.*, 
    r.score, 
    r.ratings,
    COUNT(*) OVER (PARTITION BY c.dish_base, c.dish_flavor, c.restaurant_type_std) AS frequency
    FROM {cleaned_table} c
    JOIN Menu_mds_sorted m ON c.row_id = m.row_id
    JOIN Restaurants_mds r ON m.restaurant_id = r.id
    ORDER BY c.row_id ASC
    """

    df = read_dataframe_from_sql(query, conn)
    conn.close()

    # remove combo meal
    df = df[df["is_combo"] == "False"].copy()
    return df


def calculate_and_upload(truncate: bool = False):
    """
    Calculate popularity score and upload to SQL Server.

    Parameters
    ----------
    cleaned_menu_mds : pd.DataFrame
        DataFrame containing cleaned menu data with frequency, ratings, and score.
    truncate : bool
        Whether to clear the target table before uploading.
    """
    df = combine_with_metrics()

    # Scale frequency, rating_counts, score
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(df[['frequency', 'ratings', 'score']])
    df[['freq_scaled', 'rating_scaled', 'score_scaled']] = scaled

    # Compute weighted popularity score
    df['popularity_score'] = (
        0.2 * df['freq_scaled'] +
        0.6 * df['rating_scaled'] +
        0.2 * df['score_scaled']
    )

    # Prepare for upload
    table_name = "cleaned_menu_with_popularity"
    df_to_upload = df[[
        'row_id', 'item_id', 'dish_base', 'dish_flavor', 'restaurant_type_std',
        'frequency', 'ratings', 'score', 'popularity_score'
    ]]

    # Define schema
    schema_sql = f"""
    CREATE TABLE {table_name} (
        row_id INT PRIMARY KEY,
        item_id NVARCHAR(50),
        dish_base NVARCHAR(255),
        dish_flavor NVARCHAR(255),
        restaurant_type_std NVARCHAR(255),
        frequency FLOAT,
        ratings FLOAT,
        score FLOAT,
        popularity_score FLOAT
    )
    """

    # Upload to SQL Server
    conn, cursor = connect_to_sql_server()
    try:
        create_table_if_not_exists(cursor, conn, table_name, schema_sql)

        if truncate:
            truncate_table(cursor, conn, table_name)

        records = df_to_upload.values.tolist()
        placeholders = ", ".join(["%s"] * len(df_to_upload.columns))
        insert_sql = f"""
        INSERT INTO {table_name} ({', '.join(df_to_upload.columns)})
        VALUES ({placeholders})
        """

        cursor.executemany(insert_sql, records)
        conn.commit()
        print(f"Uploaded {len(records)} rows to {table_name}")
    except Exception as e:
        conn.rollback()
        raise RuntimeError(f"Upload failed: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    calculate_and_upload(truncate = True)