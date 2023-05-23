#   xxxx.xx.xx.x:8000/admin管理員用ページ(account:menu,password:menu)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserAdmin(UserAdmin):
    list_display = ('user_account', 'user_name', 'user_email', 'is_staff', 'is_active', 'gender', 'password', 'age', 'height' , 'weight', 'gender', 'allergen')
    ordering = ('user_account',)


admin.site.register(User, UserAdmin)
