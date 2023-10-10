import pandas as pd

def my_pandas_journey_drop_columns(df, column_name):
    if column_name in df.columns:
        df = df.drop(column_name, axis=1)
        return df
    else:
        print(f"Column '{column_name}' not found in the dataframe.")
        return None

                                         


