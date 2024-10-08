# Solved on 18/08/2024
# https://leetcode.com/problems/recyclable-and-low-fat-products/

import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products[(products["low_fats"] == 'Y') & (products["recyclable"] == 'Y')][["product_id"]]
