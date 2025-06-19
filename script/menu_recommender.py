# This script generates top menu recommendations based on popularity scores.
# It filters cleaned menu records by restaurant types, averages popularity, and returns top results.
# To use it, call `recommend_menu_items(type1, type2=None, type3=None, top_n=10)`
# Requires SQL table: cleaned_menu_with_popularity → containing dish info and popularity scores.

import pandas as pd
from util_database_reader import connect_to_sql_server, read_dataframe_from_sql

def recommend_menu_items(type1: str, type2: str = None, type3: str = None, top_n: int = 10):
    """
    Recommend top menu items by popularity score across 1–3 restaurant types (averaged).

    Parameters
    ----------
    type1 : str
        Primary restaurant type.
    type2 : str, optional
        Secondary restaurant type.
    type3 : str, optional
        Tertiary restaurant type.
    top_n : int

      Number of top items to return. Must be >= 4.

    Returns
    -------
    List[Dict]
        Top N recommended items based on averaged popularity scores.
    """


    if top_n < 4:
        raise ValueError("top_n must be at least 4")
    
    # Connect and load table
    conn, _ = connect_to_sql_server()
    query = "SELECT * FROM cleaned_menu_with_popularity"
    df = read_dataframe_from_sql(query, conn)
    conn.close()

    # Filter for the selected types
    selected_types = [t for t in [type1, type2, type3] if t is not None]
    df = df[df["restaurant_type_std"].isin(selected_types)]

    if df.empty:
        return []

    # Drop duplicates (same dish showing multiple times for same type)
    df = df.sort_values("popularity_score", ascending=False).drop_duplicates(
        subset=["restaurant_type_std", "dish_base", "dish_flavor"], keep="first"
    )

    # Group by dish and average popularity score
    grouped = (df.groupby(["dish_base", "dish_flavor"], as_index=False)
                 .agg({"popularity_score": "mean"}))
    grouped = grouped.sort_values("popularity_score", ascending=False)

    # Take top N
    top_items = grouped.head(top_n)

    # Format result
    recommendations = []
    for _, row in top_items.iterrows():
        recommendations.append({
            "dish_base": row["dish_base"],
            "dish_flavor": row["dish_flavor"],
            "popularity_score": row["popularity_score"]
        })

    return recommendations


if __name__ == "__main__":
    # Test case with 3 types
    results = recommend_menu_items(type1="pizza restaurant", top_n=10)

    print("Top Recommendations:")
    for item in results:
        print(f"- {item['dish_base']} ({item['dish_flavor']}) → Popularity Score: {item['popularity_score']:.3f}")
