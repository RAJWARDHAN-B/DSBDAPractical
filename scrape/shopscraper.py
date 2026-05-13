import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
import time

url = "https://webscraper.io/test-sites/e-commerce/static"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

# print(response.status_code)

products = soup.find_all("div", class_ = "thumbnail")
# print(len(products))

data = []

customer_names = [
    "John",
    "Emma",
    "Sophia",
    "Alex",
    "David",
    "Olivia"
]

review_tags = [
    "Excellent",
    "Recommended",
    "Budget Friendly",
    "High Quality"
]

for product in products:
    title = product.find("a", class_="title")
    price = product.find("span", itemprop="price")
    description = product.find("p", class_="description")

    # rating_tag = product.find("p", attrs={"data-rating": True})
    peas = product.find_all("p")
    rating = peas[1]["data-rating"]
    # rating = rating_tag["data-rating"]
    review_count = product.find("span", itemprop="reviewCount")

    data.append({
        "title": title.text.strip(),
        "price" : price.text.strip(),
        "rating" : rating,
        "review_count" : review_count.text.strip(),
        "description" : description.text,
        "customer" : random.choice(customer_names),
        "tag" : random.choice(review_tags)
    })

    time.sleep(0.5)

df = pd.DataFrame(data)

print(data[0])

# df.to_csv("reviews_output.csv", index=False)
