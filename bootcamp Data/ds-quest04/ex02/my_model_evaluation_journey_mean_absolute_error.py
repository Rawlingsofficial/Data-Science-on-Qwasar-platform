from sklearn.metrics import mean_absolute_error
import pandas as pd

def my_model_evaluation_journey_mean_absolute_error(param_1, param_2):
    # Read specific rows and columns from the first CSV file
    a = pd.read_csv(param_1, usecols=[1, 2, 3, 4], nrows=16)
    # Read specific rows and columns from the second CSV file
    b = pd.read_csv(param_2, usecols=[1, 2, 3, 4], nrows=16)
    
    # Calculate the mean absolute error using the selected subsets of data
    mae = mean_absolute_error(a, b)
    
    # Return the mean absolute error as the output of the function
    return mae


# Define the paths of the CSV files
a = "data_1.csv"
b = "data_2.csv"

# Call the function and print the mean absolute error
#print(my_model_evaluation_journey_mean_absolute_error(a, b))
