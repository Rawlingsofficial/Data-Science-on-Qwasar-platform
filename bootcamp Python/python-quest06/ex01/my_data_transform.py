import datetime

def my_data_transform(csv_content):
    lines = csv_content.strip().split("\n")
    headers = lines[0]
    transformed_lines = [headers]

    for line in lines[1:]:
        columns = line.split(",")
        email = columns[4]
        age = int(columns[5])
        order_at = columns[9]

        # Transform email provider
        email_parts = email.split("@")
        email_provider = email_parts[1] if len(email_parts) > 1 else ""
        columns[4] = email_provider

        # Transform age
        if 1 <= age <= 20:
            columns[5] = "1->20"
        elif 21 <= age <= 40:
            columns[5] = "21->40"
        elif 41 <= age <= 65:
            columns[5] = "41->65"
        elif 66 <= age <= 99:
            columns[5] = "66->99"

        # Transform order time
        order_time = datetime.datetime.strptime(order_at, "%Y-%m-%d %H:%M:%S")
        hour = order_time.time().hour

        if 6 <= hour < 12:
            columns[9] = "morning"
        elif 12 <= hour < 18:
            columns[9] = "afternoon"
        else:
            columns[9] = "evening"

        transformed_lines.append(",".join(columns))

    return transformed_lines

# Test the function
#csv_content = "Gender,FirstName,LastName,UserName,Email,Age,City,Device,Coffee Quantity,Order At\nMale,Carl,Wilderman,carl,wilderman_carl@yahoo.com,29,Seattle,Safari iPhone,2,2020-03-06 16:37:56\nMale,Marvin,Lind,marvin,marvin_lind@hotmail.com,77,Detroit,Chrome Android,2,2020-03-02 13:55:51\nFemale,Shanelle,Marquardt,shanelle,marquardt.shanelle@hotmail.com,21,Las Vegas,Chrome,1,2020-03-05 17:53:05\nFemale,Lavonne,Romaguera,lavonne,romaguera.lavonne@yahoo.com,81,Seattle,Chrome,2,2020-03-04 10:33:53\nMale,Derick,McLaughlin,derick,mclaughlin.derick@hotmail.com,47,Chicago,Chrome Android,1,2020-03-05 15:19:48\n"

#transformed_csv = my_data_transform(csv_content)
#for line in transformed_csv:
    #print(line)
