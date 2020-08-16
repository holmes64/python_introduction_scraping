import requests
from bs4 import BeautifulSoup

load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# タグを抽出
print(soup.find("title"))
print(soup.find("h2"))
print(soup.find("li"))

# タグから文字列を抽出
print(soup.find("title").text)
print(soup.find("h2").text)
print(soup.find("li").text)


