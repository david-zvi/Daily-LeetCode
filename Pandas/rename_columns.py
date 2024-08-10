# Solved on 10/08/2024
# https://leetcode.com/problems/rename-columns/

import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    # inplace=False to run faster, no need to create a new DataFrame
    return students.rename(columns={"id":"student_id", "first":"first_name", "last":"last_name", "age":"age_in_years"}, inplace=False)
