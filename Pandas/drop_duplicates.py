# Solved on 07/08/2024
# https://leetcode.com/problems/drop-duplicate-rows/

import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(["email"])
