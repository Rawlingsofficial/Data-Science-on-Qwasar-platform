import pandas as pd
import re
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import my_ds_babel

def clean_data_1(table_1):

    df1 = pd.read_csv(table_1,sep =',')
    df1['Gender']  = df1['Gender'].replace({'0': 'Female' , '1': 'Male', 'F' : 'Female' , 'M': 'Male'})
    df1['FirstName'] = df1['FirstName'].str.replace(r'[^0-9a-zA-Z:,]+', '').str.title().astype(str)
    df1['LastName'] = df1['LastName'].str.replace(r'[^0-9a-zA-Z:,]+', '').str.title().astype(str)
    df1['Email'] = df1['Email'].str.lower()
    df1['City'] = df1['City'].str.replace(r'[^0-9a-zA-Z:,]+', '').str.title()
    df1['Age'] = df1['Age'].astype(str)
    df1['Country'] = 'USA'
    df1.drop(['UserName'], axis =1 , inplace = True)
    return df1

def clean_data_2(table_2):
    field_names = ['Age','City','Gender','Name','Email']
    df2 = pd.read_csv(table_2, sep=';',names= field_names)
    df2['Gender'] = df2['Gender'].replace({'F': 'Female', 'M': 'Male', '0': 'Female', '1': 'Male'})
    df2[['FirstName', 'LastName']] = df2['Name'].str.split(expand = True)
    df2['Email'] = df2['Email'].str.lower()
    df2['Age'] = df2['Age'].astype(str)
    df2['City'] = df2['City'].str.replace(r'[^0-9a-zA-Z:,]+', '').str.title()
    df2.drop(['Name'], axis = 1 , inplace= True)
    df2['FirstName'] =df2['FirstName'].str.replace('[^a-zA-Z]', '', regex=True).astype(str)
    df2['LastName'] =df2['LastName'].str.replace('[^a-zA-Z]', '', regex=True).astype(str)
    df2['country'] = 'USA'
    return df2
    
def clean_data_3(table_3):
    df3 = pd.read_csv(table_3 , sep = '\t|,',engine = 'python')
    df3['Gender'] = df3['Gender'].replace({'string_':'','boolean_':'','character_F':'Female','character_M' :'Male', '0': 'Female', '1': 'Male'}, regex=True)
    df3['Name'] = df3['Name'].replace({'string_': '' ,'boolean_' : '' , 'character_' : ''},regex= True)
    df3['City'] = df3['City'].str.replace(r'[^0-9a-zA-Z:,]+', '').str.title()
    df3['Email'] = df3['Email'].str.replace(r'[^0-9a-zA-Z:,]+', '').str.title()
    df3['Age'] = df3['Age'].str.replace(r'\D+', '', regex=True).astype(str)
    df3[['FirstName', 'LastName']] = df3['Name'].str.split(expand = True)
    df3.drop(['Name'], axis = 1 , inplace= True)
    df3['FirstName'] =df3['FirstName'].str.replace('[^a-zA-Z]', '', regex=True).astype(str)
    df3['LastName'] =df3['LastName'].str.replace('[^a-zA-Z]', '', regex=True).astype(str)
    df3['Country'] = 'USA'

    return df3

def merged_table(df1, df2, df3):
    result = pd.concat([df1, df2, df3], ignore_index=True)
    return result

def my_m_and_a(content_database_1, content_database_2, content_database_3):
    N_df1 = clean_data_1(content_database_1)
    N_df2 = clean_data_2(content_database_2)
    N_df3 = clean_data_3(content_database_3)
    merged_data_f = merged_table(N_df1, N_df2, N_df3)
    merged_data_f = merged_data_f[['Gender', 'FirstName', 'LastName', 'Email', 'Age', 'City', 'Country']]
    merged_data_f['FirstName'] = merged_data_f['FirstName']
    merged_data_f['LastName'] = merged_data_f['LastName']
    merged_data_f['Age'] = merged_data_f['Age']

    return merged_data_f

def main():  
    content_database_1 = 'only_wood_customer_us_1.csv'
    content_database_2 = 'only_wood_customer_us_2.csv'
    content_database_3 = 'only_wood_customer_us_3.csv'

    merged_data_f = my_m_and_a(content_database_1, content_database_2, content_database_3)
    merged_data_f.to_csv('merged_data.csv', index=False)  
    my_ds_babel.csv_to_sql('merged_data.csv', 'plastic_free_boutique.sql', 'customers')

if __name__ == '__main__':
    main()   


