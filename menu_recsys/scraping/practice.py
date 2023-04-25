import requests
from bs4 import BeautifulSoup
import re

url = "https://west2-univ.jp/sp/detail.php?t=650111&c=814167"
# url = "https://weathernews.jp/onebox/35.050126/135.787960/q=%E4%BA%AC%E9%83%BD%E5%B8%82%E5%B7%A6%E4%BA%AC%E5%8C%BA&v=f755dcb3f2c5eb660e33d08c2f6361a752e096e0c95ed7094a524287b7e0b0b1&temp=c&lang=ja"
res = requests.get(url)
if not res.ok:
    print(f"ページの取得に失敗しました。status: {res.status_code}, reason: {res.reason}")
else:
    html = res.content
    soup = BeautifulSoup(html)

    # 商品名
    dish_name = soup.select("#main > h1")[0].contents[0]
    print("dish_name: ", dish_name)

    # 商品名英語
    dish_en_name = soup.select("#main > h1")[0].contents[1].contents[0]
    print("dish_en_name: ", dish_en_name)

    # 商品画像
    image_url = soup.select("#main > div.menuImgBox > img")[0]["src"]
    print("image_url: ", image_url)

    # 値段（税込）
    price = soup.select(
        "#main > ul > li:nth-child(1) > span.price > strong"
    )[0].contents[0]
    price = re.sub(r"\D", "", price)
    print("price: ", price)
    
    # エネルギー（kcal）
    energy = soup.select(
        "#main > ul > li:nth-child(2) > span.price"
    )[0].contents[0]
    energy = re.sub(r"\D", "", energy)
    print("energy: ", energy)

    # タンパク質（g）
    protein = soup.select(
        "#main > ul > li:nth-child(3) > span.price"
    )[0].contents[0]
    protein = re.sub(r"\D", "", protein)
    print("protein: ", protein)

    # 脂質（g）
    fat= soup.select(
        "#main > ul > li:nth-child(4) > span.price"
    )[0].contents[0]
    fat = re.sub(r"\D", "", fat)
    print("fat: ", fat)

    # 炭水化物（g）
    carbohydrates = soup.select(
        "#main > ul > li:nth-child(5) > span.price"
    )[0].contents[0]
    carbohydrates = re.sub(r"\D", "",carbohydrates)
    print("carbohydrates: ", carbohydrates)

    # 食塩相当量（g）
    salt = soup.select(
        "#main > ul > li:nth-child(6) > span.price"
    )[0].contents[0]
    salt = re.sub(r"\D", "", salt)
    print("salt: ", salt)

    # カルシウム（mg）
    calcium = soup.select(
        "#main > ul > li:nth-child(7) > span.price"
    )[0].contents[0]
    calcium = re.sub(r"\D", "", calcium)
    print("calcium: ", calcium)

    # 野菜量（g）
    veg = soup.select(
        "#main > ul > li:nth-child(8) > span.price"
    )[0].contents[0]
    veg = re.sub(r"\D", "", veg)
    print("veg: ", veg)

    # 鉄（mg）
    

    # ビタミンA（μg）

    # ビタミンB1（mg）

    # ビタミン B2（mg）

    # ビタミンC（16mg）

    # 原産地（一応・・・けど使いにくいデータ形式）
    



    


    