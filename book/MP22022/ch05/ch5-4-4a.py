import csv
import requests 
from bs4 import BeautifulSoup

csvfile = "Elements.csv"
url = "https://fchart.github.io/Elements.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
with open(csvfile, 'w+', newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(["問題","答案1","答案2"])
    tags = soup.find_all("li", {"class":"question"})    
    for tag in tags:
        tag_q = tag.find("b")
        q = tag_q.text
        tags_a = tag.find_all("li", {"class":"response"})
        writer.writerow([q,tags_a[0].text,tags_a[1].text])
