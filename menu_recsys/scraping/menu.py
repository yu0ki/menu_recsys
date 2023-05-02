import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


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
        fat = soup.select(
            "#main > ul > li:nth-child(4) > span.price"
        )[0].contents[0]
        fat = re.sub(r"[^0-9.-]", "", fat)
        # print("fat: ", fat)

        # 炭水化物（g）
        carbohydrates = soup.select(
            "#main > ul > li:nth-child(5) > span.price"
        )[0].contents[0]
        carbohydrates = re.sub(r"[^0-9.-]", "", carbohydrates)
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
        allergy_list = soup.select(
            "#main > ul > li.allergy > div > ul"
        )[0].find_all("li")

        for allergy in allergy_list:
            allergies.append(allergy["class"][0][5:])
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


# 食堂ごとのメニュー一覧ページから、メニュー詳細ページへのURL一覧を取得する
"""
入力：食堂id (どの食堂のメニュー一覧を取得するか判定. 食堂idは以下のようにします)

canteen_id 対応表（仮）
中央食堂：650111
北部食堂：650113
吉田食堂：650112
ルネ：650118
（食堂メニューページのURLより）


出力：各メニューの詳細ページに飛ぶためのURL一覧（list形式）
ただし、売り切れになっている商品のURLは含まない
"""


def get_menu_urls(canteen_id: int):
    result_urls = []
    url = "https://west2-univ.jp/sp/menu.php?t=" + str(canteen_id)
    res = requests.get(url)
    if not res.ok:
        print(f"ページの取得に失敗しました。status: {res.status_code}, reason: {res.reason}")
    else:
        driver = webdriver.Chrome("./chromedriver.exe")
        driver.get(url)
        
        # トグルを展開するためのJavaScriptコード
        expand_script = '''
        var toggles = document.querySelectorAll('.toggleTitle');
        for(var i = 0; i < toggles.length; i++){
            toggles[i].click();
        }
        '''

        # JavaScriptが実行されるまで待機
        wait = WebDriverWait(driver, 20)
        toggles = wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, '.toggleTitle')
            )
        )

        # トグルを展開
        driver.execute_script(expand_script)

        # 展開が完了するまで待機
        wait.until(
            EC.invisibility_of_element_located(
                (By.CSS_SELECTOR, '.catMenu')
            )
        )

        # 展開後のHTMLを取得
        html = driver.page_source

        # BeautifulSoupオブジェクトを作成
        soup = BeautifulSoup(html, 'html.parser')

        # トグルが展開された状態でのHTMLを取得
        html = soup.prettify()

        # ブラウザを終了
        driver.quit()

        all_category = soup.find_all(True, attrs={"class": "catMenu"})
        for category_menu in all_category:
            all_menu = category_menu.find_all("a")

            for menu in all_menu:
                # 売り切れの場合はmenuのなかに「out」というクラス名のpタグが存在する
                sold_out = menu.find_all("p", {'class': 'out'})

                # 売り切れではない場合URLを取得
                if not sold_out:
                    url = menu.get("href")
                    result_urls.append("https://west2-univ.jp/sp/" + url)

        return result_urls