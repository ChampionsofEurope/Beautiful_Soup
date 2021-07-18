import requests
from bs4 import BeautifulSoup
url = 'https://www.python.org/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

print("First 4 H2 TAGS FROM PYTHON.ORG")
print(soup.find_all('a')[0:10])
