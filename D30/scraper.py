import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"

# pagination is done so I think to tackle that, we loop through the pages
# and update teh url https://books.toscrape.com/catalogue/page-1.html

response = requests.get(url)

# print(response.status_code)

soup = BeautifulSoup(response.text, "lxml")

books = soup.find_all("article", class_="product_pod")
# print(len(books))

data = []

# print (books[0])

for book in books:

    title = book.h3.a["title"]

    price = book.find("p", class_="price_color").text

    availability = book.find("p", class_="instock availability").text.strip()

    rating = book.find("p")["class"][1]

    data.append({
        "title": title,
        "price": price,
        "availability": availability,
        "rating": rating
    })

df = pd.DataFrame(data)

print(df.head())