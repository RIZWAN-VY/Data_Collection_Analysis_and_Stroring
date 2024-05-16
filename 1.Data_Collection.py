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

# WEB SCRAPING :

for i in range(1, pages + 1):

    print(f"Scraping page {i}")

    # Create URL to collect links from paginated data
    url = f"{base_url}/page/{i}/?sortby=post_date%3ADesc&pagesize={page_size}"

    # Collect HTML data from this page
    response = requests.get(url)

    # Parse content
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')