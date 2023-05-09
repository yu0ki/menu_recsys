from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


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
    user_account = models.CharField(max_length=16, unique=True, blank=False)
    user_name = models.CharField(max_length=32, unique=False)
    user_email = models.EmailField(blank=True, null=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    height = models.PositiveSmallIntegerField(blank=True, null=True)
    weight = models.PositiveSmallIntegerField(blank=True, null=True)
    gender_choices = (
        # (1, "男"),
        # (2, "女"),
        (3, "田佬"),
    )

    gender = models.PositiveSmallIntegerField(choices=gender_choices, blank=True, null=True)
    target_choices = (
        (1, "ダイエット"),
        (2, "現状を維持する"),
        (3, "体重を増やしたい"),
    )
    target = models.PositiveSmallIntegerField(choices=target_choices, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'user_account'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.user_account

