# Solved on 27/08/2024
# https://leetcode.com/problems/second-highest-salary/

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    highest_salaries = employee["salary"].drop_duplicates().sort_values(ascending=False).head(2)
    return pd.DataFrame({"SecondHighestSalary": [None] if len(highest_salaries) < 2 else [highest_salaries.iloc[1]]})
