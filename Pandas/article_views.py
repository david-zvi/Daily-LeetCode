# Solved on 20/08/2024 - making up for 19/08/2024
# https://leetcode.com/problems/article-views-i/

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return views[views["author_id"] == views["viewer_id"]][["author_id"]]
    .drop_duplicates()
    .rename(columns = {"author_id": "id"})
    .sort_values("id")
