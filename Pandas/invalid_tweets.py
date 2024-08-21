# Solved on 21/08/2024
# https://leetcode.com/problems/invalid-tweets/

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets[tweets["content"].str.len() > 15][["tweet_id"]]
