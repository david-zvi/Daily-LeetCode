# Solved on 17/08/2024 - making up for 15/08/2024
# https://leetcode.com/problems/reshape-data-melt/

import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return report.melt(id_vars="product", var_name="quarter", value_name="sales")
