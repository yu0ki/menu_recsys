import requests
from bs4 import BeautifulSoup

url = "https://weather.yahoo.co.jp/weather/jp/26/6110.html"
res = requests.get(url)
if not res.ok:
    print(f"ページの取得に失敗しました。status: {res.status_code}, reason: {res.reason}")
else:
    html = res.content
    soup = BeautifulSoup(html)
    # print(soup)
    elems = soup.select("#main > div.forecastCity > table > tr > td > div > p.pict > img")[0].attrs["alt"]
    print(elems)