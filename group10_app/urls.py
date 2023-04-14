"""
URL configuration for group10_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from menu_recsys.views import home, signup, login, user_home, search, recommend


urlpatterns = [
    path("admin/", admin.site.urls),
    # ログイン前のページ（ログインページへのリンクなどを貼る）
    path("/", home),
    # サインアップ
    path('signup', signup),
    # ログイン
    path('login', login),
    # ユーザマイページ
    path("user_home/", user_home),
    # 検索条件設定ページ
    path("search", search),
    # 検索結果ページ
    path("recommend", recommend)
]
