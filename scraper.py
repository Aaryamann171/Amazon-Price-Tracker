import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.in/BenQ-23-8-inch-Monitor-Built/dp/B073NTCT4Q/ref=sr_1_3?keywords=24+inch+monitor&qid=1567673325&s=gateway&sr=8-3'

headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle")

print(title)