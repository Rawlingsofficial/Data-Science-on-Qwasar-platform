import pandas as pd

def my_pandas_journey_group_by(df, column_name):
    if column_name in df.columns:
        result = df.groupby(column_name)
        return result
    else:
        print(f"Column '{column_name}' not found in the dataframe.")
        return None
       

