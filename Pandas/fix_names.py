# Solved on 24/08/2024 - making up for 23/08/2024
# https://leetcode.com/problems/fix-names-in-a-table/

import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users["name"] = users["name"].str.capitalize()
    return users.sort_values("user_id")