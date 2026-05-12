import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
import time

url = "https://webscraper.io/test-sites/e-commerce/static"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

# print(response.status_code)

products = soup.find_all("div", class_ = "produce_wrapper")

data = []

