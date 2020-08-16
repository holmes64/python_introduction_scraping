import requests
from bs4 import BeautifulSoup
import urllib

load_url = "https://news.yahoo.co.jp/categories/it"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

filename = "linklist.txt"
with open(filename, "w") as f:
    # Classで検索し、その中のすべてのaタグを検索して表示する
    topic = soup.find(class_="topicsList_main")
    for element in topic.find_all("a"):
        url = element.get("href")
        link_url = urllib.parse.urljoin(load_url, url)
        f.write(element.text+"\n")
        f.write(link_url+"\n")
        f.write("\n")
