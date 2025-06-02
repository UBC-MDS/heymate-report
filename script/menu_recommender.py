import pandas as pd
from sql_reader import connect_to_sql_server, read_dataframe_from_sql

def recommend_menu_items(type1: str, type2: str = None, type3: str = None, top_n: int=5):
    """
    Recommend top menu items by popularity score from cleaned_menu_with_popularity table.

    Parameters
    ----------
    type1 : str
        Primary restaurant type.
    type2 : str, optional
        Secondary restaurant type.
    type3 : str, optional
        Tertiary restaurant type.
    top_n : int
        Number of top items to return per type.

    Returns
    -------
    List[Dict]
        Recommended items grouped by restaurant type.
    """
    # Connect and load table from SQL Server
    conn, _ = connect_to_sql_server()
    query = "SELECT * FROM cleaned_menu_with_popularity"
    df = read_dataframe_from_sql(query, conn)
    conn.close()

    # Group by restaurant_type_std
    grouped = dict(tuple(df.groupby("restaurant_type_std")))
    selected_types = [t for t in [type1, type2, type3] if t is not None]

    recommendations = []
    for rest_type in selected_types:
        matches = grouped.get(rest_type, pd.DataFrame())
        if matches.empty:
            continue

        top_items = matches.nlargest(top_n, "popularity_score")
        recommendations.append({
            'restaurant_type': rest_type,
            'recommended_items': top_items[['dish_base', 'dish_flavor', 'popularity_score']].to_dict(orient='records')
        })

    return recommendations


if __name__ == "__main__":
    results = recommend_menu_items(type1="breakfast restaurant", top_n=10)
    for group in results:
        print(f"Recommendations for {group['restaurant_type']}:")
        for item in group["recommended_items"]:
            print(f"- {item['dish_base']} ({item['dish_flavor']}) → Popularity Score: {item['popularity_score']:.3f}")

