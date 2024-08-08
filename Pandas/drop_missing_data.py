# Solved on 08/08/2024
# https://leetcode.com/problems/drop-missing-data/

import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=["name"])
