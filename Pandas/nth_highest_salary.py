# Solved on 26/08/2024
# https://leetcode.com/problems/nth-highest-salary/

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    n_unique_biggest = employee["salary"].drop_duplicates().sort_values(ascending=False).head(N)
    column_title = "getNthHighestSalary(" + str(N) + ")"
    if N < 0 or len(n_unique_biggest) < N: 
        return pd.DataFrame(data={column_title: [None]})
    return pd.DataFrame(data={column_title: [n_unique_biggest.min()]})
