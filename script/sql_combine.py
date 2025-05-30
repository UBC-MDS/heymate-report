import pandas as pd
from sql_reader import connect_to_sql_server, read_dataframe_from_sql

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
    SELECT c.*, r.score, r.ratings
    FROM {cleaned_table} c
    JOIN Menu_mds_sorted m ON c.row_id = m.row_id
    JOIN Restaurants_mds r ON m.restaurant_id = r.id
    """

    df = read_dataframe_from_sql(query, conn)
    conn.close()
    return df

if __name__ == "__main__":
    try:
        df = combine_with_metrics()
        print("Combined DataFrame loaded successfully:")
        print(df.head()) 
    except Exception as e:
        print(f"Error during test: {e}")