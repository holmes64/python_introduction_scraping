import requests

url = "https://www.ymori.com/books/python2nen/test1.html"
response = requests.get(url)

response.encoding = response.apparent_encoding

print(response.text)
print("-------------------------")
print(response.url)
print("-------------------------")
print(response.content)
print("-------------------------")
print(response.apparent_encoding)
print("-------------------------")
print(response.status_code)
print("-------------------------")
print(response.headers)
print("-------------------------")
