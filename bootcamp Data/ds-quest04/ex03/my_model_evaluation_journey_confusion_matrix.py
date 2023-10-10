from sklearn.metrics import confusion_matrix

def my_model_evaluation_journey_confusion_matrix(param_1, param_2):
    # Calculate the confusion matrix based on the input parameters
    cm = confusion_matrix(param_1, param_2)
    
    # Return the confusion matrix as the output of the function
    return cm


# Define the input parameters for calculating the confusion matrix
param_1 = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
param_2 = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]

# Call the function and print the confusion matrix
#print(my_model_evaluation_journey_confusion_matrix(param_1, param_2))
