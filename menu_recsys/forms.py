from django.contrib.auth.forms import forms
from models import Menu, Canteen, History_order


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ["dish_url", "canteen", "dish_name", "dish_en_name", "image_url", "price",
                  "energy", "protein", "fat", "carbohydrates", "salt", "calcium", "veg",
                  "iron", "vitamin_a", "vitamin_b1", "vitamin_b2", "vitamin_c", "place_of_origin",
                  "allergies"]
        labels = {
            "dish_url": "料理のリンク",
            "canteen": "食堂ID",
            "dish_name": "料理名",
            "dish_en_name": "英語の料理名",
            "image_url": "商品画像のリンク",
            "price": "組価(税込)",
            "energy": "エネルギー",
            "protein": "タンパク質",
            "fat": "脂質",
            "carbohydrates": "炭水化物",
            "salt": "食塩相当量",
            "calcium": "カルシウム",
            "veg": "野菜量",
            "iron": "鉄",
            "vitamin_a": "ビタミン A",
            "vitamin_b1": "ビタミン B1",
            "vitamin_b2": "ビタミン B2",
            "vitamin_c": "ビタミン C",
            "place_of_origin": "原産地",
            "allergies": "アレルギー"
        }
