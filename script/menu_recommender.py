# import pandas as pd
# from sql_reader import connect_to_sql_server, read_dataframe_from_sql

# def recommend_menu_items(type1: str, type2: str = None, type3: str = None, top_n: int=5):
#     """
#     Recommend top menu items by popularity score from cleaned_menu_with_popularity table.

#     Parameters
#     ----------
#     type1 : str
#         Primary restaurant type.
#     type2 : str, optional
#         Secondary restaurant type.
#     type3 : str, optional
#         Tertiary restaurant type.
#     top_n : int
#         Number of top items to return per type.

#     Returns
#     -------
#     List[Dict]
#         Recommended items grouped by restaurant type.
#     """
#     # Connect and load table from SQL Server
#     conn, _ = connect_to_sql_server()
#     query = "SELECT * FROM cleaned_menu_with_popularity"
#     df = read_dataframe_from_sql(query, conn)
#     conn.close()

#     # Remove duplicates
#     df = df.sort_values("popularity_score", ascending=False).drop_duplicates(
#     subset=["restaurant_type_std", "dish_base", "dish_flavor"], keep="first"
#     )

#     # Group by restaurant_type_std
#     grouped = dict(tuple(df.groupby("restaurant_type_std")))
#     selected_types = [t for t in [type1, type2, type3] if t is not None]

#     recommendations = []
#     for rest_type in selected_types:
#         matches = grouped.get(rest_type, pd.DataFrame())
#         if matches.empty:
#             continue

#         top_items = matches.nlargest(top_n, "popularity_score")
#         recommendations.append({
#             'restaurant_type': rest_type,
#             'recommended_items': top_items[['dish_base', 'dish_flavor', 'popularity_score']].to_dict(orient='records')
#         })

#     return recommendations


# if __name__ == "__main__":
#     results = recommend_menu_items(type1="Pizza restaurant", top_n=10)
#     for group in results:
#         print(f"Recommendations for {group['restaurant_type']}:")
#         for item in group["recommended_items"]:
#             print(f"- {item['dish_base']} ({item['dish_flavor']}) → Popularity Score: {item['popularity_score']:.3f}")


import pandas as pd
from sql_reader import connect_to_sql_server, read_dataframe_from_sql

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
        Number of top items to return.

    Returns
    -------
    List[Dict]
        Top N recommended items based on averaged popularity scores.
    """
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
    results = recommend_menu_items(type1="pizza restaurant", type2="burger joint", type3="sandwich shop", top_n=10)
    print("Top Recommendations:")
    for item in results:
        print(f"- {item['dish_base']} ({item['dish_flavor']}) → Popularity Score: {item['popularity_score']:.3f}")
