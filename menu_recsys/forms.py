#   ユーザフォーム

from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth.forms import forms
from .models import Menu, Canteen, History_order


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['user_account']
        labels = {
            'user_account': 'アカウント名（必須)'
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_name', 'user_email', 'age', 'height', 'weight', 'gender', 'target', 'momentum']
        labels = {
            'user_email': 'メールアドレス',
            'user_name': 'ニックネーム(必須)',
            'age': '年齢',
            'height': '身長(cm)',
            'weight': '体重(kg)',
            'gender': '性別',
            'target': '目標',
            'momentum': '運動習慣',
        }


class UserAllergenForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['allergen']
        labels = {
            'allergen': 'アレルゲン'
        }





class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ["dish_url", "canteen", "dish_name", "dish_en_name", "image_url", "price",
                  "energy", "protein", "fat", "carbohydrates", "salt", "calcium", "veg",
                  "iron", "vitamin_a", "vitamin_b1", "vitamin_b2", "vitamin_c", "place_of_origin",
                  "allergies", "image"]
        labels = {
            "dish_url": "料理のリンク",
            "canteen": "食堂ID",
            "dish_name": "料理名",
            "dish_en_name": "英語の料理名",
            "image_url": "商品画像のリンク",
            "image": "画像",
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
