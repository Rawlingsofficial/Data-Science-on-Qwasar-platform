# Welcome to My Select Query
Create a class MySelectQuery.
Your constructor will receive a CSV content (as a string), first line will be the name of the column.
Example:
"name,year_start,year_end,position,height,weight,birth_date,college\nAlaa Abdelnaby,1991,1995,F-C,6-10,240,'June 24, 1968',Duke University\nZaid Abdul-Aziz,1969,1978,C-F,6-9,235,'April 7, 1946',Iowa State University\nKareem Abdul-Jabbar,1970,1989,C,7-2,225,'April 16, 1947','University of California, Los Angeles
Mahmoud Abdul-Rauf,1991,2001,G,6-1,162,'March 9, 1969',Louisiana State University\n"
It will be prototyped:
constructor(csv_content)
Implement a where method which will take 2 arguments: column_name and value.
It will return an array of strings which matches the value.
It will be prototyped:
where(column_name, criteria)
Our examples will use these CSV
Nba Player Data
Nba Players
Nba Seasons Stats
Example00
Input: "name" && "Andre Brown"
Output: ["Andre Brown,2007,2009,F,6-9,245,birth_date,May 12, 1981,'DePaul University'"]

## Task
What is the problem? And where is the challenge?
The problem statement in the task you provided is to implement a simple query tool,
 MySelectQuery, that can load CSV data and filter rows based on specific criteria. The challenge
  lies in correctly parsing the CSV content, storing it in a suitable data structure, and implementing 
  the filtering logic to retrieve the desired results.

## Description
How have you solved the problem?
The MySelectQuery class has the following methods:
__init__(self, csv_content)
The constructor initializes the MySelectQuery object. It takes the CSV content as a string and sets up the data structure to store the rows.
The CSV content string is split into lines using the splitlines() method.
The first line, which contains the column names, is extracted and stored in the columns attribute.
The remaining lines, representing the data rows, are processed and stored in the data attribute.
where(self, column_name, criteria)
The where method filters the data rows based on the specified column and criteria.
It retrieves the index of the specified column_name from the columns attribute using the index() method. This index will be used to access the corresponding value in each row.
It initializes an empty result list to store the matching rows.
It iterates over each row in the data attribute.
For each row, it checks if the value at the specified column index matches the criteria.
If there is a match, the row is joined into a string using ','.join(row) and added to the result list.
Once all rows have been processed, the result list is returned.
## Installation
How to install your project? npm install? make? make re?
there was no instalation for this project
## Usage
How does it work?
To use MySelectQuery, create an instance of the class by passing the CSV content as a string to the constructor:
csv_content = "name,year_start,year_end,position,height,weight,birth_date,college\nAlaa Abdelnaby,1991,1995,F-C,6-10,240,'June 24, 1968',Duke University\nZaid Abdul-Aziz,1969,1978,C-F,6-9,235,'April 7, 1946',Iowa State University\nKareem Abdul-Jabbar,1970,1989,C,7-2,225,'April 16, 1947','University of California, Los Angeles\nMahmoud Abdul-Rauf,1991,2001,G,6-1,162,'March 9, 1969',Louisiana State University\n"
query = MySelectQuery(csv_content)
```
./my_project argument1 argument2
```

### The Core Team


<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px'></span>
