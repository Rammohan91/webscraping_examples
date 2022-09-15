import imp
import requests
from bs4 import BeautifulSoup

r = requests.get("https://timesofindia.indiatimes.com/?from=mdr")
c = r.content

soup = BeautifulSoup(c, "html.parser")
all = soup.find_all("figcaption")
print(all.prettify())