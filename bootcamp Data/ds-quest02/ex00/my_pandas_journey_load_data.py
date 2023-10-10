import pandas as pd
from io import StringIO

def my_pandas_journey_load_data(param_1):
    # Convert the StringIO object to a string
    csv_string = param_1.getvalue()

    # Read the CSV string into a DataFrame
    df = pd.read_csv(StringIO(csv_string))

    # Return the DataFrame
    return df
