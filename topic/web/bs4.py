import requests
from bs4 import BeautifulSoup

## Note: see also soupsieve

url = "https://fchart.github.io/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

tags = soup("a") 
tag = tags[12]
print("URL網址: ", tag.get("href", None))
print("標籤內容: ", tag.text)
print("target屬性: ", tag["target"])

# More example
'''
soup.find("a") 
soup.find_all("a", attrs={"class": "sister"})
'''