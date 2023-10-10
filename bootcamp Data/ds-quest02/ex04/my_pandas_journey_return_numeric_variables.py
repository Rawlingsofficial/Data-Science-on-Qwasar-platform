import pandas as pd
import numpy as np

def my_pandas_journey_return_numeric_variables(param_1):
    # Select the numeric variables from the DataFrame
    numeric_variables = param_1.select_dtypes(include=[np.number])

    # Return the selected numeric variables
    return numeric_variables
