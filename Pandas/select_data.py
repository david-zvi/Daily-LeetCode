# Solved on 06/08/2024 - making up for 05/08/2024
# https://leetcode.com/problems/select-data/

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students["student_id"] == 101][["name", "age"]]
