from sklearn.metrics import recall_score

def my_model_evaluation_journey_recall_score(param_1, param_2):
    # Calculate the recall score based on the input parameters
    # The `average=None` parameter ensures that the recall score is computed for each class separately
    scores = recall_score(param_1, param_2, average=None)
    
    # Return the recall scores for each class as the output of the function
    return scores


# Define the input parameters for calculating the recall scores
param_1 = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
param_2 = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]

# Call the function and print the recall scores
#print(my_model_evaluation_journey_recall_score(param_1, param_2))
