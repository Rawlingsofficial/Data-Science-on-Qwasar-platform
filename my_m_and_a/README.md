# Welcome to My M And A
You've worked as a Junior Data Engineer at Plastic Free Boutique for three months.
Your first mission was to build a strong, robust, and scalable customers database 
for the exponential growth the company will soon have. Your manager is delighted.
We've just acquired a new company, Only Wood Box, which will be a perfect solution
 for our packaging department. They are experts in making wood packages at a competitive,
  light, and cheap price.
Expert in their technology, they didn't believe in the digital world.
 Despite the decent number of customers, they didn't have to invest in their infrastructure.
  Before quitting, their engineer told us that at least we had stored all the information; 
  I don't understand what he meant.
## Task
What is the problem? And where is the challenge?
in this project the cript that performs diffrent tasked is related to
 (data cleaning, merging , and conversion)
 conversion will be  done between csv and sqlite db format
## Description
How have you solved the problem?
1 DATA CLEANING :
clean_data_1 Function:
Reads data from table_1 (only_wood_1 CSV file).
Standardizes "Gender" to "Female" or "Male."
Cleans and title-cases "FirstName," "LastName," "City," and "Email."
Sets "Country" to 'USA.'
Drops "UserName."
clean_data_2 Function:
Reads data from table_2 (only_wood_2 CSV file).
Standardizes "Gender" to "Female" or "Male."
Splits "Name" into "FirstName" and "LastName."
Cleans and lower-cases "Email" and title-cases "City."
Sets "Country" to 'USA.'
clean_data_3 Function:
Reads data from table_3 (only_wood_3 CSV file).
Standardizes "Gender."
Extracts "FirstName" and "LastName" from "Name."
Cleans and title-cases "City" and "Email."
Extracts numerical digits from "Age."
Sets "Country" to 'USA.'
2 DATA MERGING:
Concatenates three cleaned DataFrames (df1, df2, df3) into a single DataFrame "result."
Ignores index values.
Combines data from three input tables into one.
3 DATA MERGING
my_m_and_a Function:
Orchestrates the entire process.
Calls the cleaning functions for three input CSV files, resulting in three cleaned DataFrames.
Uses the merged_table function to merge these DataFrames into one.
The final merged DataFrame has columns: 'Gender', 'FirstName', 'LastName', 'Email', 'Age', 'City', and 'Country.'
Converts data in 'FirstName', 'LastName', and 'Age' columns to strings using astype.
## Installation
How to install your project? npm install? make? make re?
there were no main instalation during the couse of this project.
mainly importing python libries
## Usage
<<<<<<< HEAD
After merging the data and storing it in merged_df
merged_df.to_csv('merged_data.csv', index=False)  
my_ds_babel.csv_to_sql('merged_data.csv', 'plastic_free_boutique.sql', 'customers')
///print(merged_df)   RUNING THIS SCRIPT WILL SHOW THE CONTENTS OF THE MERGE DF

=======
How does it work?
After merging the data and storing it in merged_df
merged_df.to_csv('merged_data.csv', index=False)  
my_ds_babel.csv_to_sql('merged_data.csv', 'plastic_free_boutique.sql', 'customers')
print(merged_df)   RUNING THIS SCRIPT WILL SHOW THE CONTENTS OF THE MERGE DF
```
>>>>>>> f077ac60e83ff3f739e4f5350ead2c73e474f744
./my_project argument1 argument2

### The Core Team


<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px'></span>
