#   ユーザモデル

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from multiselectfield import MultiSelectField
from multiselectfield.validators import MaxValueMultiFieldValidator


class UserManager(BaseUserManager):
    def create_user(self, user_account, password=None, **extra_fields):
        if not user_account:
            raise ValueError('アカウントを入力してください（必須）')
        user = self.model(user_account=user_account, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, user_account, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(user_account, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    user_account = models.CharField(max_length=16, unique=True, blank=False)  # user_account
    user_name = models.CharField(max_length=32, unique=False)
    user_email = models.EmailField(blank=True, null=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    height = models.PositiveSmallIntegerField(blank=True, null=True)
    weight = models.PositiveSmallIntegerField(blank=True, null=True)
    gender_choices = (
        (1, "男"),
        (2, "女"),
        (3, "その他"),
    )
    gender = models.PositiveSmallIntegerField(choices=gender_choices, blank=True, null=True)
    target_choices = (
        (4, "ダイエット"),
        (5, "現状を維持する"),
        (6, "体重を増やしたい"),
    )
    target = models.PositiveSmallIntegerField(choices=target_choices, blank=True, null=True)
    allergen_choices = (
        (1, "卵"),
        (2, "牛乳"),
        (3, "落花生"),
        (4, "そば"),
        (5, "小麦"),
        (6, "えび"),
        (7, "かに"),
        (8, "あわび"),
        (9, "いか"),
        (10, "いくら"),
        (11, "さけ"),
        (12, "さば"),
        (13, "牛肉"),
        (14, "鶏肉"),
        (15, "豚肉"),
        (16, "大豆"),
        (17, "松茸"),
        (18, "山芋"),
        (19, "オレンジ"),
        (20, "桃"),
        (21, "キウイフルーツ"),
        (22, "りんご"),
        (23, "くるみ"),
        (24, "ゼラチン"),
        (25, "バナナ"),
        (26, "ゴマ"),
        (27, "カシューナッツ"),
    )
    allergen = MultiSelectField(choices=allergen_choices, max_choices=27, validators=[MaxValueMultiFieldValidator(27)])
    momentum_choices = (
        (1, "運動はほぼしない 生活の大部分が座位"),
        (2, "普通 座位中心、通勤・通学・家事での移動、軽いスポーツをしている"),
        (3, "活発 移動が多い、立ち仕事、運動習慣あり"),
    )
    momentum = models.PositiveSmallIntegerField(choices=momentum_choices, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'user_account'
    REQUIRED_FIELDS = []
    objects = UserManager()


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
