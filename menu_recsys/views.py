from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

from menu_recsys.forms import SignUpForm, UserProfileForm, UserAllergenForm
from django.contrib import messages
from menu_recsys.models import User, History_order
from .decorators import user_account_required
from menu_recsys.database_update import database_update
from menu_recsys.models import Menu, Canteen
from .order_recognition.image_processors import object_detect
from django.http import HttpResponse
import urllib
from django.shortcuts import get_object_or_404
import tweepy
from menu_recsys.scraping.weather import get_weather_info
from menu_recsys.recommendation import menu_recommendation
from functools import reduce
import datetime
import pandas as pd
from django.shortcuts import HttpResponse, redirect
from django.db.models import Q
from django.views.generic import View
from django.core.paginator import Paginator


ALLERGEN_JP2EN = {
    "卵": "egg",
    "牛乳": "milk",
    "落花生": "peanut",
    "そば": "soba",
    "小麦": "wheat",
    "えび": "seafood",
    "かに": "seafood",
    "あわび": "seafood",
    "いか": "seafood",
    "いくら": "seafood",
    "さけ": "seafood",
    "さば": "seafood",
    "牛肉": "beef",
    "鶏肉": "chicken",
    "豚肉": "pork",
    "大豆": "soybean",
    "松茸": "matsutake",
    "山芋": "potato",
    "オレンジ": "orange",
    "桃": "peach",
    "キウイフルーツ": "kiwi fruit",
    "りんご": "apple",
    "くるみ": "walnut",
    "ゼラチン": "gelatin",
    "バナナ": "banana",
    "ゴマ": "sesame",
    "カシューナッツ": "nut"
}


# ログイン前ホーム画面
def home(request):
    return redirect("login")
    pass


# ログイン・サインアップ関連
# サインアップ
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("../login/")

        else:
            print(form.errors)
            print(form.errors.get_json_data())
            values = form.errors.get_json_data().values()
            for value in values:
                for v in value:
                    messages.error(request, v["message"])
    else:
        form = SignUpForm()
    return render(request, "pages/signup.html", {"form": form})
  


# ログイン
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user_account = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, user_account=user_account, password=password)
            if user is not None:
                login(request, user)
                return redirect('user_home', user.user_account)

    else:
        form = AuthenticationForm()
    return render(request, "pages/login.html", {"form": form})
  

# ログアウト
def logout_view(request):
    logout(request)
    return redirect("../login")


# 　ユーザ身分確認
# ユーザホーム
@user_account_required
def user_home(request, user_account):
    user = get_object_or_404(User, user_account=user_account)
    #history = get_object_or_404(History_order, user_account=user_account)
    #history = History.objects.filter(user_account = user_account,...,....)
    weather = get_weather_info()
    #s = History_order.objects.get()
    #history.get_deferred_fields
    ctx = {
        "weather": weather["weather"],
        "max_temp": weather["max_temperature"][0],
        "min_temp": weather["min_temperature"][0],
        "panda_type": user.target, #4:slim, 5:nutral, 6:muscleの3つ
        "panda_status": "fine", #fine, notgood, fatの3つ?
        "user": user
    }
    
    return render(request, "pages/user_home.html", ctx)


def user_info_input(request):
    pass


# # ユーザホーム
# def user_home(request):
#     ctx = {
#         "weather": "曇り時々",
#         "max_temp": "28℃",
#         "min_temp": "14℃",
#         "panda_type": "nutral", #nutral, slim, muscleの3つ?
#         "panda_status": "fine", #fine, notgood, fatの3つ?
#     }
#     return render(request, 'pages/user_home.html', ctx)


# 検索条件入力
def search(request, user_account):
    if request.method == "GET":
        context = {
            "canteen_name_choices": Canteen.canteen_name_choices,
        }
        return render(request, "pages/search.html", context=context)
    budget = request.POST.get("budget")
    canteen = request.POST.get("canteen")
    target = request.POST.get("target")
    # user_id = "60"
    # user_allergen = ["milk"]
    # user_gender = 1
    user_id = User.objects.get(user_account=user_account).id
    user_gender = User.objects.get(id=user_id).gender
    if len(User.objects.get(id=user_id).allergen) == 0:
        menus = Menu.objects.filter(canteen__canteen_name=canteen) \
            .exclude(history_order__order_date__gt=datetime.date.today() - datetime.timedelta(7),
                     history_order__user_id=user_id)
    else:
        user_allergen = [ALLERGEN_JP2EN[User.allergen_choices[int(i)-1][1]] for i in User.objects.get(id=user_id).allergen]
        menus = Menu.objects.filter(canteen__canteen_name=canteen) \
            .exclude(reduce(lambda x, y: x | y, [Q(allergies__icontains=item) for item in user_allergen])) \
            .exclude(history_order__order_date__gt=datetime.date.today() - datetime.timedelta(7),
                     history_order__user_id=user_id)
    menus_ = list()
    menus_index = list()
    for menu in menus:
        menus_.append([menu.id, menu.price, menu.protein, menu.carbohydrates, menu.veg])
        menus_index.append(menu.id)
    menus_columns = ["id", "price", "protein", "carbohydrates", "veg"]
    menus = pd.DataFrame(data=menus_, index=menus_index, columns=menus_columns)
    menu_id = menu_recommendation.recommending(menus, max_number=5, max_price=budget, gender=user_gender, momentum=target)
    return recommend(request, menu_id=menu_id)

    # x = database_update.canteen_database_update()


# 検索結果
def recommend(request, menu_id=None):
    if menu_id is None:
        menu = Menu.objects.all()
    else:
        menu_id = menu_id[0]
        menu = Menu.objects.filter(reduce(lambda x, y: x | y, [Q(id=item) for item in menu_id]))
    return render(request, "pages/recommend.html", {"menu": menu})

@user_account_required
def profile(request, user_account):
    user = get_object_or_404(User, user_account=user_account)
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            return redirect("user_home", user.user_account)
        else:
            print(form.errors)

    else:
        form = UserProfileForm(instance=user)

    context = {
        "form": form, "user": user
    }
    return render(request, "pages/profile.html", context)


@user_account_required
def allergen(request, user_account):
    user = get_object_or_404(User, user_account=user_account)
    if request.method == "POST":
        form = UserAllergenForm(request.POST, instance=user)
        if form.is_valid():
            allergen_value = form.cleaned_data.get('allergen', 'default_value')
            form.instance.allergen = allergen_value
            user = form.save()
            return redirect("user_home", user.user_account)
        else:
            print(form.errors)

    else:
        form = UserAllergenForm(instance=user)

    context = {
        "form": form, "user": user
    }
    return render(request, "pages/allergen.html", context)


def dame(request):
    return render(request, "pages/dame.html")

# カメラページ
# ストリーミング画像・映像を表示するview
def camera(request):
    return render(request, 'pages/camera.html', {})


# 撮った写真を表示
def lunch_photo(request):
    # Base64エンコードされた画像データ取得
    base64_image = request.POST.get('image')

    # データベースからメニュー情報取得
    # TODO: searchページと連携して食堂を絞り込む
    # Menu database から image_urlとdish_nameを取得してdict型に変換
    menus = list(Menu.objects.all().values("image_url", "dish_name", "id"))

    # 画像処理
    detected_dish_info = object_detect(base64_image, menus)

    return render(request, 
                  'pages/lunch_photo.html', 
                  {'image': base64_image,
                   "detected_dish_info": detected_dish_info,
                   "menus": menus})


# 撮った写真から食べた献立を特定し、データベースに保存
def submit_lunch(request):
    pass
    # lunch_photo経由で送られてきた画像を取得
    base64_image = request.POST.get('image')

    # POSTで送られてきたメニューidから
    # メニュー名を全て取得
    dish_id = request.POST.get('dish-0')
    dishes = []
    dish_ids = []
    while dish_id is not None:
        dish_name = get_object_or_404(Menu, id=dish_id).dish_name
        dishes.append(dish_name)
        dish_ids.append(dish_id)
        dish_id = request.POST.get('dish-' + str(len(dishes)))

    # データベースに保存
    for dish_id in dish_ids:
        data = {
            'user': request.user,
            'dish': Menu.objects.get(id=dish_id),
        }
        History_order.objects.create(**data)


    
    # renderでそれっぽい画面を返す
    return render(request, 
                  'pages/submit_lunch.html', 
                  {'image': base64_image,
                   "detected_dish_info": dishes,
                #    "twitter_share_url": url
                   })


def history_order(request):
    print(History_order.objects.filter(user=request.user))
    return render(request,
                  'pages/history_order.html', 
                  {
                      'history_orders': History_order.objects.filter(user=request.user)
                  }
    )

def update_menu_database(request):
    # データ更新
    # TODO: add image 
    database_update.canteen_database_update()
    return HttpResponse("Updating menu database was finished!")
