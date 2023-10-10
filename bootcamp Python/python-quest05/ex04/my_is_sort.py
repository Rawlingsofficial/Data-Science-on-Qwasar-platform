def my_is_sort(param_1):
    if len(param_1) <= 1:
        return True

    # Check if the array is sorted in ascending order
    is_ascending = all(param_1[i] <= param_1[i+1] for i in range(len(param_1)-1))
    if is_ascending:
        return True

    # Check if the array is sorted in descending order
    is_descending = all(param_1[i] >= param_1[i+1] for i in range(len(param_1)-1))
    if is_descending:
        return True

    return False

# Test cases
#print(my_is_sort([1, 1, 2]))           # Output: True
#print(my_is_sort([2, 1, -1]))          # Output: True
#print(my_is_sort([4, 7, 0, 3]))        # Output: False
#print(my_is_sort([]))                  # Output: True
