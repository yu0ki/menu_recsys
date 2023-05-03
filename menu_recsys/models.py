from django.db import models


# Create your models here.
class User(models.Model):
    user_account = models.CharField(verbose_name="アカウント", max_length=16, unique=True, blank=False)
    user_name = models.CharField(verbose_name="名前", max_length=32, unique=False, default=user_account)
    user_pwd = models.CharField(verbose_name="パスワード", max_length=16, default="pwd", blank=False, null=False)
    user_email = models.EmailField(verbose_name="メール", null=True, blank=True)
    age = models.PositiveSmallIntegerField(verbose_name="年齢", null=True, blank=True)
    height = models.PositiveSmallIntegerField(verbose_name="身長", null=True, blank=True)
    weight = models.PositiveSmallIntegerField(verbose_name="体重", null=True, blank=True)
    gender_choices = (
        (1, "男"),
        (2, "女"),
        (3, "その他")
    )
    gender = models.PositiveSmallIntegerField(verbose_name="性別", choices=gender_choices, null=True, blank=True)
    create_time = models.DateTimeField(verbose_name="アカウント作成時間")
    allergen = models.CharField(verbose_name="アレルゲン", max_length=128, null=True, blank=True)


class Canteen(models.Model):
    """Canteen table
    Name  :   ID
    中央食堂：650111
    北部食堂：650113
    吉田食堂：650112
    ルネ：650118"""

    canteen_id = models.CharField(verbose_name="食堂ID", max_length=8, primary_key=True)
    canteen_name_choices = (
        (1, "中央食堂"),
        (2, "北部食堂"),
        (3, "吉田食堂"),
        (4, "ルネ")
    )
    canteen_name = models.PositiveSmallIntegerField(verbose_name="食堂名", choices=canteen_name_choices, default=1)
    canteen_location = models.CharField(verbose_name="食堂の場所", max_length=64)
    canteen_url = models.URLField(verbose_name="食堂リンク")


class Menu(models.Model):
    """Menu Table"""
    dish_url = models.URLField(verbose_name="料理のリンク")
    canteen = models.ForeignKey(verbose_name="食堂ID", to="Canteen", to_field="canteen_id", on_delete=models.CASCADE)
    dish_name = models.CharField(verbose_name="料理名", max_length=64, blank=False, null=False, default="Unknown")
    dish_en_name = models.CharField(verbose_name="英語の料理名", max_length=256, null=True, blank=True)
    image_url = models.URLField(verbose_name="商品画像のリンク", null=True, blank=True)
    price = models.PositiveSmallIntegerField(verbose_name="組価(税込)", null=True, blank=True)
    energy = models.PositiveSmallIntegerField(verbose_name="エネルギー", null=True, blank=True)
    protein = models.FloatField(verbose_name="タンパク質", null=True, blank=True)
    fat = models.FloatField(verbose_name="脂質", null=True, blank=True)
    carbohydrates = models.FloatField(verbose_name="炭水化物", null=True, blank=True)
    salt = models.FloatField(verbose_name="食塩相当量", null=True, blank=True)
    calcium = models.IntegerField(verbose_name="カルシウム", null=True, blank=True)
    veg = models.IntegerField(verbose_name="野菜量", null=True, blank=True)
    iron = models.FloatField(verbose_name="鉄", null=True, blank=True)
    vitamin_a = models.IntegerField(verbose_name="ビタミン A", null=True, blank=True)
    vitamin_b1 = models.FloatField(verbose_name="ビタミン B1", null=True, blank=True)
    vitamin_b2 = models.FloatField(verbose_name="ビタミン B2", null=True, blank=True)
    vitamin_c = models.IntegerField(verbose_name="ビタミン C", null=True, blank=True)
    place_of_origin = models.CharField(verbose_name="原産地", max_length=64, blank=True, null=False, default="Unknown")
    allergies = models.CharField(verbose_name="アレルギー", max_length=64, null=True, blank=True)


class History_order(models.Model):
    """Users' history order table"""
    user = models.ForeignKey(verbose_name="ユーザID", to="User", to_field="id", on_delete=models.CASCADE)
    dish = models.ForeignKey(verbose_name="料理ID", to="Menu", to_field="id", on_delete=models.CASCADE)
    order_date = models.DateField(verbose_name="注文日", auto_now_add=True)
