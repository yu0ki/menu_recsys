from menu_recsys.models import Canteen, Menu
from menu_recsys.scraping.menu import get_menu_info, get_menu_urls
import logging
import time
import traceback
from django.core.files import File
import requests
from io import BytesIO

CANTEEN_ID = {
    1: 650111,
    2: 650113,
    3: 650112,
    4: 650118
}

logging.basicConfig(level='INFO', filename='./scraping_log.log', filemode='a+')


def canteen_database_update(canteen_id=None):
    """Update all the canteen info"""
    if canteen_id is not None:
        print("Start updating canteen {}".format(canteen_id))
        canteen_name = {v: k for k, v in CANTEEN_ID.items()}[canteen_id]
        canteen_url = "https://west2-univ.jp/sp/menu.php?t=" + str(canteen_id)
        Canteen.objects.create(canteen_id=canteen_id, canteen_name=canteen_name, canteen_url=canteen_url)
        menu_database_update(canteen_id)
    else:
        for canteen_name, canteen_id in CANTEEN_ID.items():
            print("Start updating canteen {}".format(canteen_id))
            if not Canteen.objects.filter(canteen_id=canteen_id).exists():
                canteen_url = "https://west2-univ.jp/sp/menu.php?t=" + str(canteen_id)
                Canteen.objects.create(canteen_id=canteen_id, canteen_name=canteen_name, canteen_url=canteen_url)
            menu_database_update(canteen_id)
    return True


def menu_database_update(canteen_id: int) -> None:
    """update the menu"""
    menu_urls = get_menu_urls(canteen_id=canteen_id)
    for menu_url in menu_urls:
        menu_info = None
        canteen = Canteen.objects.get(canteen_id=str(canteen_id))
        try:
            menu_info = get_menu_info(url=menu_url)
        except Exception as e:
            logging.error(time.strftime('%y-%m-%d %H:%M:%S') + traceback.format_exc() + '\n{}\n'.format(menu_url))
            if type(e) is IndexError:
                logging.info('Trying to crawling the data again without dish_en_name\n')
                menu_info = get_menu_info(url=menu_url, en_name_exists=False)
        finally:
            if menu_info is not None:
                if not Menu.objects.filter(dish_name=menu_info["dish_name"], canteen=canteen).exists() and \
                        not Menu.objects.filter(dish_url=menu_url, canteen=canteen).exists():
                    canteen = Canteen.objects.get(canteen_id=str(canteen_id))
                    for key, value in menu_info.items():
                        if value == "-":
                            menu_info[key] = 0
                    # 画像取得
                    image_response = requests.get(menu_info["image_url"])
                    Menu.objects.create(dish_url=menu_url,
                                        canteen=canteen,
                                        dish_name=menu_info["dish_name"],
                                        dish_en_name=menu_info["dish_en_name"],
                                        image_url=menu_info["image_url"],
                                        price=int(menu_info["price"]),
                                        energy=int(menu_info["energy"]),
                                        protein=float(menu_info["protein"]),
                                        fat=float(menu_info["fat"]),
                                        carbohydrates=float(menu_info["carbohydrates"]),
                                        salt=float(menu_info["salt"]),
                                        calcium=int(float(menu_info["calcium"])),
                                        veg=int(menu_info["veg"]),
                                        iron=float(menu_info["iron"]),
                                        vitamin_a=int(menu_info["vitamin_a"]),
                                        vitamin_b1=float(menu_info["vitamin_b1"]),
                                        vitamin_b2=float(menu_info["vitamin_b2"]),
                                        vitamin_c=int(menu_info["vitamin_c"]),
                                        place_of_origin=str(menu_info["place_of_origin"]),
                                        allergies=",".join(menu_info["allergies"])).image.save(menu_info["dish_name"] + '.jpg', File(BytesIO(image_response.content)), save=True)
                    logging.info('Successfully write the data into database\n--------------\n')
            else:
                logging.error("Cannot get the data without dish_en_name\n--------------\n")
