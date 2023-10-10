import csv

class MySelectQuery:
    def __init__(self, csv_content):
        self.data = []
        reader = csv.reader(csv_content.splitlines())
        self.columns = next(reader)  # Store the column names
        for row in reader:
            self.data.append(row)  # Store the data rows
    
    def where(self, column_name, criteria):
        column_index = self.columns.index(column_name)  # Find the index of the specified column
        result = []
        for row in self.data:
            if row[column_index] == criteria:  # Check if the value in the specified column matches the criteria
                result.append(','.join(row))  # Join the row elements into a string and add it to the result
        return result



#creat instance
#csv_content = "name,year_start,year_end,position,height,weight,birth_date,college\nAlaa Abdelnaby,1991,1995,F-C,6-10,240,'June 24, 1968',Duke University\nZaid Abdul-Aziz,1969,1978,C-F,6-9,235,'April 7, 1946',Iowa State University\nKareem Abdul-Jabbar,1970,1989,C,7-2,225,'April 16, 1947','University of California, Los Angeles\nMahmoud Abdul-Rauf,1991,2001,G,6-1,162,'March 9, 1969',Louisiana State University\n"
#query = MySelectQuery(csv_content)

#result = query.where("name", "Andre Brown")
#print(result)

#output 
#["Andre Brown,2007,2009,F,6-9,245,birth_date,May 12, 1981,'DePaul University'"]
