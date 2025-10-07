import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import Workbook


# URL of the website to scrape
url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"

# Step 1: Send a request to the website
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Step 2: Find all product (property) containers
items = soup.find_all("div", class_="thumbnail")

data = []
for item in items:
    title = item.find("a", class_="title").text.strip()
    price = item.find("h4", class_="price float-end card-title pull-right").text.strip()
    description = item.find("p", class_="description").text.strip()
    link = "https://webscraper.io" + item.find("a", class_="title")["href"]

    data.append({
        "Title": title,
        "Price": price,
        "Description": description,
        "Link": link
    })

# Step 3: Convert to DataFrame
df = pd.DataFrame(data)

# Step 4: Save to Excel
df.to_excel("real_estate_data.xlsx", index=False)

print("✅ Data scraped and saved successfully as 'real_estate_data.xlsx'")
