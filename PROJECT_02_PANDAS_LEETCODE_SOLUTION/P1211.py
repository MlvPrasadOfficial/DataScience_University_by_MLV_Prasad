import pandas as pd

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    # Add the 'ratio' column
    queries["ratio"] = queries["rating"] / queries["position"]

    # Group by 'query_name' and compute the metrics
    df = queries.groupby("query_name").agg(
        quality=("ratio", lambda x: round(x.mean(), 2)),
        poor_query_percentage=(
            "rating",
            lambda x: float(round(100 * sum(x < 3) / len(x), 2))
        )
    )
    
    # Reset index and sort by 'quality' descending and 'query_name' as secondary
    return df