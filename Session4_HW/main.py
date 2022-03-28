import csv
import requests
from bs4 import BeautifulSoup
from webtoon import search

TOON_URL = f'https://comic.naver.com/webtoon/weekdayList?week=mon'

toon_html = requests.get(TOON_URL)
toon_page = requests.get(TOON_URL)
toon_page_parsing = BeautifulSoup(toon_page.text, "html.parser")

toon_list_box = toon_page_parsing.find("ul", {"class":"img_list"})
toon_list = toon_list_box.find_all("li")

result_list = search(toon_list)

file = open('toonlist.csv', mode = "w", newline='')

writer = csv.writer(file)

writer.writerow(["제목", "작가", "별점"])

for result in result_list:
    row = []
    row.append(result["title"])
    row.append(result["author"])
    row.append(result["rating"])
    writer.writerow(row)
