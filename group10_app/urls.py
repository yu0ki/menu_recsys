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
from menu_recsys.views import Camera
from menu_recsys.views import lunch_photo


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    path("signup/", signup, name='signup'),
    path("login/", login_view, name="login"),
    path('user_home/<str:user_account>/', views.user_home, name='user_home'),
    path("search/", search),
    path("recommend/", recommend),
    path('profile/<str:user_account>/', views.profile, name="profile"),
    path("dame/", dame, name="dame"),
    path("logout/", logout_view, name="logout"),
    path('allergen/<str:user_account>/', views.allergen, name="allergen"),
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
    path("recommend", recommend),
    # カメラページ
    path('camera', Camera.as_view(), name="camera"),
    # # 映像をストリーミング
    # path('video_feed', video_feed_view(), name="video_feed"),
    # 撮った写真を表示
    path('lunch_photo', lunch_photo, name="lunch_photo"),
]
