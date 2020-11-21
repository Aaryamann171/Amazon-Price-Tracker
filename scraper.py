import requests
from bs4 import BeautifulSoup as bs

URL = "https://www.amazon.in/BenQ-23-8-inch-Monitor-Built/dp/B073NTCT4Q/ref=sr_1_3?keywords=24+inch+monitor&qid=1567673325&s=gateway&sr=8-3"

headers = {
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}


def price_checker():
    page = requests.get(URL, headers=headers)
    soup = bs(page.content, "lxml")
    title = soup.find(id="productTitle")
    price = soup.find(id="priceblock_ourprice").get_text()
    price_adjusted = price.replace(",", "")
    converted_price = float(price_adjusted[2:7])
    print("Here is the current price: " + price_adjusted)
    if(converted_price < 10000):
        # Todo: send mail via SMTP server
        print("Sending mail")


price_checker()
