import requests
from bs4 import BeautifulSoup

load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# すべてのliタグを検索して、その文字列を表示する
for element in soup.find_all("li"):
    print(element.text)

# ID検索
chap2 = soup.find(id="chap2")
print(chap2)

# IDで検索し、その中のすべてのliタグを検索して表示する
for element in chap2.find_all("li"):
    print(element.text)
