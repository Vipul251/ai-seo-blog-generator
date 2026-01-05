import requests
from bs4 import BeautifulSoup

def scrape_products():
    url = "https://books.toscrape.com/catalogue/category/books_1/index.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    products = []
    for item in soup.select(".product_pod")[:3]:
        products.append({
            "title": item.h3.a["title"],
            "price": item.select_one(".price_color").text,
            "rating": item.p["class"][1]
        })
    return products
