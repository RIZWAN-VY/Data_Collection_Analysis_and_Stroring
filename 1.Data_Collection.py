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

        # WEB SCRAPING : SKYTRAX Website
#------------------------------------------------------------------------------------------------
for i in range(1, pages + 1):

    print(f"Scraping page {i}")

    # Create URL to collect links from paginated data
    url = f"{base_url}/page/{i}/?sortby=post_date%3ADesc&pagesize={page_size}"

    # Collect HTML data from this page
    response = requests.get(url)

    # Parse content
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')

        # DATA COLLECTION : Collecting 3790 Reviews From SKYTRAX Website
#------------------------------------------------------------------------------------------------
    # Collecting all customer names
    for item in soup.find_all("span", itemprop= "name"):
        names.append(item.get_text())     
        if len(names) == 3790:
            break

    # Collecting all customer location
    for item in soup.find_all("h3", class_="text_sub_header userStatusWrapper"):
        location_text = item.get_text()
        start_index = location_text.find("(") + 1
        end_index = location_text.find(")")
        location = location_text[start_index:end_index]
        locations.append(location.strip())         
        if len(locations) == 3790:
            break
        
    # Collecting all date published
    for item in soup.find_all("time", itemprop ="datePublished"):
        date_review_posted.append(item.get_text())       
        if len(date_review_posted) == 3790:
            break
        
    # Collecting all rating
    for index, item in enumerate(soup.find_all("span", itemprop="ratingValue")):
        if index != 0:  # Skip the first rating because first rating in website is overall rating
            rating.append(item.get_text().strip())         
            if len(rating) == 3790:
                break
        
    # Collecting all review title
    for item in soup.find_all("h2", class_="text_header"):
        review_title.append(item.get_text())       
        if len(review_title) == 3790:
            break
        
    # Collecting all detailed review 
    for item in soup.find_all("div", class_ ="text_content"):
        detailed_review.append(item.get_text())
        if len(detailed_review) == 3790:
            break
        
    # Collecting all recommended
    for item in soup.find_all("td", class_=["review-value rating-yes","review-value rating-no"]):
        recommended.append(item.get_text())
        if len(recommended) == 3790:
            break
        
'''
print("Names:",len(names))
print("Locations:", len(locations))
print("Date Review Posted:", len(date_review_posted))
print("Ratings:", len(rating))
print("review_title:", len(review_title))
print("Detailed review",len(detailed_review))
print("Recommended:", len(recommended))
'''
