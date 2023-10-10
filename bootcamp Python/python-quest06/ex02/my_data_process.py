import json

def my_data_process(param_1):
    columns = param_1[0].split(",")  # Extract column names from the header
    data = {}

    for line in param_1[1:]:
        values = line.split(",")

        for i in range(len(columns)):
            column = columns[i]
            value = values[i]

            if column in ["FirstName", "LastName", "UserName", "Coffee Quantity"]:
                continue

            if column not in data:
                data[column] = {}

            if value not in data[column]:
                data[column][value] = 0

            data[column][value] += 1

    result = json.dumps(data)
    return result.replace(", ", ",").replace(": ", ":").replace("'", '"')


