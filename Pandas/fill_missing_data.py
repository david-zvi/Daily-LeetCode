# Solved on 12/08/2024
# https://leetcode.com/problems/fill-missing-data/

import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products.fillna({"quantity": 0}, inplace=True)
    return products
