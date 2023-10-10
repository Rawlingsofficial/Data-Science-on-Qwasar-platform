import pandas as pd

def my_pandas_journey_return_n_sample_rows(param_1, param_2):
    # Get a sample of the specified number of rows from the DataFrame
    sample_rows = param_1.sample(n=param_2)

    # Return the sample rows
    return sample_rows
