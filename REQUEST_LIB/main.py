import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.tvcnews.tv/")
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)

# cat = soup.a
# for x in cat:
#     print(x)
