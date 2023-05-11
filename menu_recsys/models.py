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

    def __str__(self):
        return self.user_account
