import requests
from bs4 import BeautifulSoup
page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
print(page)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())
list(soup.children)
