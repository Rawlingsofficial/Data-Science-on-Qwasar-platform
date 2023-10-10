from sklearn.metrics import f1_score

def my_model_evaluation_journey_f_one(param_1, param_2):
    # Calculate the F1 score based on the input parameters
    # The `average=None` parameter ensures that the F1 score is computed for each class separately
    scores = f1_score(param_1, param_2, average=None)
    
    # Return the F1 scores for each class as the output of the function
    return scores


# Define the input parameters for calculating the F1 scores
param_1 = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
param_2 = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]

# Call the function and print the F1 scores
#print(my_model_evaluation_journey_f_one(param_1, param_2))
