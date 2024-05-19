"""
    DATA CLEANING AND STORING
======================================================================================================================================
"""
# Libraries
import pandas as pd

# # Loading the Data
data = pd.read_csv('C:/Users/rizwa/Rizwan/Projects/Data_Collection_and_Storage/2.British_Airways_Customer_reviews.csv')
# print(data) 


#   DATA CLEANING
#====================================================================================================================================

# checking Data types and columns
# print(data.dtypes)
'''
Customer_Names        object
Customer_Locations    object
Date_Review_Posted    object
Ratings                int64
Recommended           object
Review                object
Detailed_Review       object
'''

#   Cleaning Review and Detailed_Review column 
#====================================================================================================================================

unwanted_phrases = ['✅', 'Trip Verified', '|', 'Not Verified']

# Remove the unwanted phrases
for phrase in unwanted_phrases:
    data['Detailed_Review'] = data['Detailed_Review'].str.replace(phrase, '', regex=False)

data['Detailed_Review'] = data['Detailed_Review'].str.strip()   # Remove leading and trailing whitespaces
data['Review'] = data['Review'].str.strip() 


# Converting data type of  Date_Review_Posted (Object) to datetime
#====================================================================================================================================
data['Date_Review_Posted'] = pd.to_datetime(data['Date_Review_Posted'], errors='coerce')
