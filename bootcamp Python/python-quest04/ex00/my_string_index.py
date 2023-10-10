def my_string_index(haystack, needle):
    for i in range(len(haystack)):
        if haystack[i] == needle:
            return i
    return -1

# Test cases
#print(my_string_index("hello", "l"))    # Output: 2
#print(my_string_index("aaaaa", "b"))    # Output: -1
