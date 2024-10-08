# Solved on 20/08/2024
# https://leetcode.com/problems/customers-who-never-order/

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    return customers[~customers["id"].isin(orders["customerId"])][["name"]].rename(columns={"name": "Customers"})
