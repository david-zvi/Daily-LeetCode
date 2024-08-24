# Solved on 24/08/2024
# https://leetcode.com/problems/find-users-with-valid-e-mails/

import pandas as pd
import re

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    # Regex match function
    return users[users["mail"].str.match(r"^[A-Za-z][A-Za-z0-9_\.\-]*@leetcode\.com$")]
