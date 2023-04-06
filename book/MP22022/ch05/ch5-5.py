import requests 
from bs4 import BeautifulSoup
import csv

url = "https://www.w3schools.com/html/html_media.asp"
csvfile = "VideoFormat.csv"
r = requests.get(url)
r.encoding = "utf8"
soup = BeautifulSoup(r.text, "html.parser")
tag_table = soup.select_one("table.w3-table-all.notranslate")  # 找到<table>
rows = tag_table.find_all("tr")   # 找出所有<tr>
# 開啟CSV檔案寫入截取的資料
with open(csvfile, 'w+', newline='', encoding="utf-8") as fp:
    writer = csv.writer(fp)
    for row in rows:
        lst = []
        for cell in row.find_all(["td", "th"]):
            lst.append(cell.text.replace("\n","").replace("\r",""))
        writer.writerow(lst)

