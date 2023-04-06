import requests
from bs4 import BeautifulSoup
import csv 

url = "https://movies.yahoo.com.tw/movie_thisweek.html?page=1"

def save_to_csv(items, file):
    with open(file, "w+", newline="", encoding="utf-8") as fp:
        writer = csv.writer(fp)
        for item in items:
            writer.writerow(item)
r = requests.get(url)
if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text, "html.parser")
    movies = [["中文片名","英文片名","期待度","海報圖片","上映日"]]
    root = soup.select_one("#content_l > div.release_box > ul")
    rows = root.find_all("li")
    for row in rows:
        info = row.find("div",{"class":"release_info"})
        name = info.find("div",{"class": "release_movie_name"})
        c_name = info.find("a").text
        e_name = info.find("div",{"class":"en"}).find("a").text
        expect = info.find("div",{"class": "leveltext"})
        if (expect):
            expect = expect.find("span").text
        else:
            expect = "None" 
        photo = row.find("div",{"class": "release_foto"})
        poster_url = photo.find("img")["src"]
        r_date = info.find('div',{"class":"release_movie_time"}).text        
        movie= [c_name.strip(),
                e_name.strip(),
                expect.strip(),
                poster_url.strip(),
                r_date.strip()[7:]]
        movies.append(movie)
    for movie in movies:
        print(movie)    
    save_to_csv(movies, "movies.csv")    
else:
    print("HTTP請求錯誤...")





   
    
