import requests
import csv
from bs4 import BeautifulSoup
import time
import re

start = time.time()
for i in range(62):
    main_URL = 'https://apps.shopify.com/postscript-sms-marketing/reviews?page='
    URL = main_URL+str(i)

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id='Main')
    reviews = results.find_all('div', class_="review-listing")

    with open("ps_reviews_updated_new.txt", "a", newline="") as f:
        for review in reviews:
            shop = review.find('div', class_="review-listing-header")
            content = review.find('div', class_="truncate-content-copy")
            star = review.find("div", class_="review-metadata__item-value")
            

            display_name = shop.text.strip() + "\n"*2
            display_text = content.text.strip() + "\n"*2
            display_star = star.text.strip() + "\n"*2
           

            print()

            f.write("Shop Name: ")
            f.write(display_name)
            f.write("Star: ")
            f.write(display_star)
            f.write("Review Content: ")
            f.write(display_text)
            
            

done = time.time()
elapsed = done - start

print(elapsed)
