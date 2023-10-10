def my_csv_parser(param_1, param_2):
    lines = param_1.split("\n")
    result = []

    for line in lines:
        if line:
            columns = line.split(param_2)
            result.append(columns)

    return result

# Test case
#csv_string = "a,b,c,e\n1,2,3,4\n"
#separator = ","
#parsed_csv = my_csv_parser(csv_string, separator)
#print(parsed_csv)
# Output: [['a', 'b', 'c', 'e'], ['1', '2', '3', '4']]
