# Solved on 17/08/2024
# https://leetcode.com/problems/big-countries/

import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world[(world["area"] >= 3000000) | (world["population"] >= 25000000)][["name", "population", "area"]]
