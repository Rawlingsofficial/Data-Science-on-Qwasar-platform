import numpy as np

def my_numpy_journey_array_full_random(param_1, param_2):
    # Create a NumPy array filled with random integers
    numpy_array = np.random.randint(low=0, high=100, size=(param_1, param_2))

    # Return the NumPy array
    return numpy_array
