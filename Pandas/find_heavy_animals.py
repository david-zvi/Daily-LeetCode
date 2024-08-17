# Solved on 17/08/2024 - making up for 16/08/2024
# https://leetcode.com/problems/method-chaining/

import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals["weight"] > 100].sort_values(by="weight", ascending=False)[["name"]]
