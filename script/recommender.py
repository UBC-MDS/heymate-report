import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sql_combine import combine_with_metrics
from sql_reader import connect_to_sql_server, read_dataframe_from_sql
from pprint import pprint


def recommend_menu_items(cleaned_menu_mds):
    df = combine_with_metrics(cleaned_menu_mds)
    recommendations = []

    # Step 1: Scale frequency, ratings, score
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(df[['frequency', 'ratings', 'score']])
    df[['freq_scaled', 'rating_scaled', 'score_scaled']] = scaled

    # Step 2: Compute weighted popularity score
    df['popularity_score'] = (
        0.2 * df['freq_scaled'] +
        0.6 * df['rating_scaled'] +
        0.2 * df['score_scaled']
    )

    # Step 3: Group Uber Eats data by standardized restaurant type
    grouped_clean = dict(tuple(df.groupby("restaurant_type_std")))

    # Step 4: Match each internal restaurant with top N items from similar type
    for _, row in cleaned_internal_menu_mds.iterrows():
        rest_type = row['restaurant_type_std']
        matches = grouped_clean.get(rest_type, pd.DataFrame())

        if matches.empty:
            continue

        top_items = matches.nlargest(top_n, "popularity_score")

        recommendations.append({
        
            'restaurant_type': rest_type,
            'recommended_items': top_items[['dish_base', 'dish_flavor', 'popularity_score']].to_dict(orient='records')
        })

    return recommendations



