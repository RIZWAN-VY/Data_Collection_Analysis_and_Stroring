'''
    DATA COLLECTION USING WEB SCRAPING
'''
# Libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://www.airlinequality.com/airline-reviews/british-airways"
pages = 38
page_size = 100

# Columns :

names = []
locations = []
date_review_posted = []
rating = []
review_title = []  
detailed_review = []
recommended = []