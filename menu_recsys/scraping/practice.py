import requests
from bs4 import BeautifulSoup
import re

# メニュー詳細ページから、１つのメニューの詳細情報を取得する関数
# 入力：メニューURL
def get_menu_info(url: str):

    # url = "https://west2-univ.jp/sp/detail.php?t=650111&c=814167"
    res = requests.get(url)
    if not res.ok:
        print(f"ページの取得に失敗しました。status: {res.status_code}, reason: {res.reason}")
    else:
        html = res.content
        soup = BeautifulSoup(html)

        # 商品名
        dish_name = soup.select("#main > h1")[0].contents[0]
        # print("dish_name: ", dish_name)

        # 商品名英語
        dish_en_name = soup.select("#main > h1")[0].contents[1].contents[0]
        # print("dish_en_name: ", dish_en_name)

        # 商品画像
        image_url = soup.select("#main > div.menuImgBox > img")[0]["src"]
        # print("image_url: ", image_url)

        # 値段（税込）
        price = soup.select(
            "#main > ul > li:nth-child(1) > span.price > strong"
        )[0].contents[0]
        price = re.sub(r"[^0-9.-]", "", price)
        # print("price: ", price)
        
        # エネルギー（kcal）
        energy = soup.select(
            "#main > ul > li:nth-child(2) > span.price"
        )[0].contents[0]
        energy = re.sub(r"[^0-9.-]", "", energy)
        # print("energy: ", energy)

        # タンパク質（g）
        protein = soup.select(
            "#main > ul > li:nth-child(3) > span.price"
        )[0].contents[0]
        protein = re.sub(r"[^0-9.-]", "", protein)
        # print("protein: ", protein)

        # 脂質（g）
        fat= soup.select(
            "#main > ul > li:nth-child(4) > span.price"
        )[0].contents[0]
        fat = re.sub(r"[^0-9.-]", "", fat)
        # print("fat: ", fat)

        # 炭水化物（g）
        carbohydrates = soup.select(
            "#main > ul > li:nth-child(5) > span.price"
        )[0].contents[0]
        carbohydrates = re.sub(r"[^0-9.-]", "",carbohydrates)
        # print("carbohydrates: ", carbohydrates)

        # 食塩相当量（g）
        salt = soup.select(
            "#main > ul > li:nth-child(6) > span.price"
        )[0].contents[0]
        salt = re.sub(r"[^0-9.-]", "", salt)
        # print("salt: ", salt)

        # カルシウム（mg）
        calcium = soup.select(
            "#main > ul > li:nth-child(7) > span.price"
        )[0].contents[0]
        calcium = re.sub(r"[^0-9.-]", "", calcium)
        # print("calcium: ", calcium)

        # 野菜量（g）
        veg = soup.select(
            "#main > ul > li:nth-child(8) > span.price"
        )[0].contents[0]
        veg = re.sub(r"[^0-9.-]", "", veg)
        # print("veg: ", veg)

        # 鉄（mg）
        iron = soup.select(
            "#main > ul > li:nth-child(9) > span.price"
        )[0].contents[0]
        iron = re.sub(r"[^0-9.-]", "", iron)
        # print("iron: ", iron)

        # ビタミンA（μg）
        vitamin_a = soup.select(
            "#main > ul > li:nth-child(10) > span.price"
        )[0].contents[0]
        vitamin_a = re.sub(r"[^0-9.-]", "", vitamin_a)
        # print("vitamin_a: ", vitamin_a)


        # ビタミンB1（mg）
        vitamin_b1 = soup.select(
            "#main > ul > li:nth-child(11) > span.price"
        )[0].contents[0]
        vitamin_b1 = re.sub(r"[^0-9.-]", "", vitamin_b1)
        # print("vitamin_b1: ", vitamin_b1)
        

        # ビタミン B2（mg）
        vitamin_b2 = soup.select(
            "#main > ul > li:nth-child(12) > span.price"
        )[0].contents[0]
        vitamin_b2 = re.sub(r"[^0-9.-]", "", vitamin_b2)
        # print("vitamin_b2: ", vitamin_b2)
        

        # ビタミンC（16mg）
        vitamin_c = soup.select(
            "#main > ul > li:nth-child(13) > span.price"
        )[0].contents[0]
        vitamin_c = re.sub(r"[^0-9.-]", "", vitamin_c)
        # print("vitamin_c: ", vitamin_c)
        

        # 原産地（一応・・・けど使いにくいデータ形式）
        place_of_origin = soup.select(
            "#main > ul > li:nth-child(14) > span.price"
        )[0].contents[0]
        # print("place_of_origin: ", place_of_origin)


        # アレルギー（リスト形式）
        allergies = []
        allegy_list = soup.select(
            "#main > ul > li.allergy > div > ul"
        )[0].find_all("li")

        for allegy in allegy_list:
            allergies.append(allegy["class"][0][5:])
        # print("allergies", allergies)

        return {
            "dish_name": dish_name,
            "dish_en_name": dish_en_name,
            "image_url": image_url,
            "price": price,
            "energy": energy,
            "protein": protein,
            "fat": fat,
            "carbohydrates": carbohydrates,
            "salt": salt,
            "calcium": calcium,
            "veg": veg,
            "iron": iron,
            "vitamin_a": vitamin_a,
            "vitamin_b1": vitamin_b1,
            "vitamin_b2": vitamin_b2,
            "vitamin_c": vitamin_c,
            "place_of_origin": place_of_origin,
            "allergies": allergies,
        }







        


        