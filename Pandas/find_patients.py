# Solved on 25/08/2024
# https://leetcode.com/problems/patients-with-a-condition/

import pandas as pd
import re

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    # Check if conditions contains DIAB1 as a prefix of a word - \b represents
    # a beggining of a word in Regex
    return patients[patients["conditions"].str.contains(r"\bDIAB1")]
