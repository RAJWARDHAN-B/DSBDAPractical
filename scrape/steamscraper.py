import requests
import pandas as pd

url = "https://store.steampowered.com/appreviews/730?json=1"

response = requests.get(url)

data = response.json()

reviews = data["reviews"]

output = []

for review in reviews:

    author = review["author"]["steamid"]
    text = review["review"]
    rating = "Recommended" if review["voted_up"] else "Not Recommended"
    upvotes = review["votes_up"]
    timestamp = review["timestamp_created"]

    output.append({
        "Customer_ID": author,
        "Review": text,
        "Rating": rating,
        "Upvotes": upvotes,
        "Timestamp": timestamp
    })

df = pd.DataFrame(output)

print(df.head())

# df.to_csv("steam_reviews.csv", index=False)