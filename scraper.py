import requests
import csv
from bs4 import BeautifulSoup
import time


#calculate how long it takes to ruin this (see math and print at bottom)
start = time.time()

#loop thru all review pages

for i in range(100):
    main_URL = 'https://apps.shopify.com/postscript-sms-marketing/reviews?page='
    URL = main_URL+str(i)

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id='Main')
    reviews = results.find_all('div', class_="review-listing")

    with open("ps_reviews.csv", "a", newline="") as f:
        writer = csv.writer(f)
        for review in reviews:
            shop = review.find('div', class_="review-listing-header")
            content = review.find('div', class_="truncate-content-copy")
            star = review.find("div", class_="review-metadata__item-value")
            

            display_name = shop.text.strip() + "\n"*2
            display_text = content.text.strip() + "\n"*2
            display_star = star.text.strip() + "\n"*2
           

            #print([display_name, display_star, display_text])

            writer.writerow([display_name, display_star, display_text])
            
            

done = time.time()
elapsed = done - start

print(elapsed)
