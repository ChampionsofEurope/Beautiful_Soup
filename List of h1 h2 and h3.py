import requests
from bs4 import BeautifulSoup
url = 'https://www.python.org/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

print("Tags for h1,h2 and h3")
for heading in soup.find_all(["h1","h2","h3"]):
    print(heading.name + ' ' + heading.text.strip())
