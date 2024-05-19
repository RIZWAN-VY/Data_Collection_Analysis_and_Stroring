"""
    DATA CLEANING AND STORING
======================================================================================================================================
"""
# Libraries
import pandas as pd
from textblob import TextBlob

# Loading the Data
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


# Adding a column for Sentiment of Review [Positive, Neutral, Negative]
#====================================================================================================================================
reviews = data['Review'] + ' ' + data['Detailed_Review']

# Calculate sentiment scores
Sentiments = []
for text in reviews:
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    Sentiments.append(sentiment)
# print(Sentiments)           # Polarity Score of the the reviews

# Categorize sentiments
Sentiments_category = []
for score in Sentiments:
    if score > 0.1:
        Sentiments_category.append("Positive")
    elif score < 0.1:
        Sentiments_category.append("Negative")
    else:
        Sentiments_category.append("Neutral")
# print(Sentiments_category)

data['Review_Sentiment'] = Sentiments_category

#====================================================================================================================================