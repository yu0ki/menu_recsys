import requests
from bs4 import BeautifulSoup

url = "https://www.jma.go.jp/bosai/forecast/#area_type=class20s&area_code=2610000"
res = requests.get(url)
if not res.ok:
    print(f"ページの取得に失敗しました。status: {res.status_code}, reason: {res.reason}")
else:
    html = res.content
    soup = BeautifulSoup(html)
    # print(soup)
    elems = soup.select("#short-table-container > div > div > div > div.contents-wide-table-scroll > table > tr:nth-of-type(4) > td:nth-of-type(1)")
    print(elems)