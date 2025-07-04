import pandas as pd

def run(data: pd.DataFrame):
    # Placeholder: implement stress scenarios
    stressed = data.copy()
    stressed['PolicyValue'] *= 0.9  # Simulate 10% loss
    return stressed.describe()
