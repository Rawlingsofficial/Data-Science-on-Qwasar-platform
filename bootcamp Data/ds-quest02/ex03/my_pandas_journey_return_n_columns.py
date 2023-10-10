def my_pandas_journey_return_n_columns(param_1, param_2):
    # Extract the columns up to the nth column
    result = param_1.iloc[:, :param_2]

    # Return the extracted columns
    return result
