from menu_recsys.models import Canteen, Menu
from ..scraping.menu import get_menu_info, get_menu_urls

CANTEEN_ID = {
    "中央食堂": 650111,
    "北部食堂": 650113,
    "吉田食堂": 650112,
    "ルネ": 650118
}


def canteen_database_update():
    for canteen_name, canteen_id in CANTEEN_ID.items():
        if not Canteen.objects.filter(canteen_id=canteen_id).exists():
            canteen_url = "https://west2-univ.jp/sp/menu.php?t=" + str(canteen_id)
            Canteen.objects.create(canteen_id=canteen_id, canteen_name=canteen_name,
                                   canteen_url=canteen_url)
            menu_database_update(canteen_id)
    pass


def menu_database_update(canteen_id):
    menu_urls = get_menu_urls(canteen_id=canteen_id)
    for menu_url in menu_urls:
        if not Menu.objects.filter(dish_name=menu_url["dish_name"]).exists() and not Menu.objects.filter(
                dish_url=menu_url).exists():
            menu_info = get_menu_info(url=menu_url)
            Menu.objects.create(canteen_id=canteen_id,
                                dish_name=menu_info["dish_name"],
                                dish_en_name=menu_info["dish_en_name"],
                                price=menu_info["price"],
                                energy=menu_info["energy"],
                                protein=menu_info["protein"],
                                fat=menu_info["fat"],
                                carbohydrates=menu_info["carbohydrates"],
                                salt=menu_info["salt"],
                                calcium=menu_info["calcium"],
                                veg=menu_info["veg"],
                                iron=menu_info["iron"],
                                vitaminA=menu_info["vitamin_a"],
                                vitaminB1=menu_info["vitamin_b1"],
                                vitaminB2=menu_info["vitamin_b2"],
                                vitaminC=menu_info["vitamin_c"],
                                place_of_origin=menu_info["place_of_origin"],
                                allergies=menu_info["allergies"])
            print("Adding {} to DB……".format(menu_info["dish_name"]))
