from sklearn.metrics import r2_score
import pandas as pd

def my_model_evaluation_journey_r2_score(param_1, param_2):
    # Read specific rows and columns from the first CSV file
    a = pd.read_csv(param_1, usecols=[1, 2, 3, 4], nrows=16)
    # Read specific rows and columns from the second CSV file
    b = pd.read_csv(param_2, usecols=[1, 2, 3, 4], nrows=16)
    
    # Calculate the R2 score using the selected subsets of data
    r2 = r2_score(a, b)
    
    # Return the R2 score as the output of the function
    return r2


# Define the paths of the CSV files
a = "data_1.csv"
b = "data_2.csv"

# Call the function and print the R2 score
#print(my_model_evaluation_journey_r2_score(a, b))
