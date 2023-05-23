from django.shortcuts import render
from menu_recsys.models import User, Menu, Canteen
from menu_recsys.database_update import database_update
from menu_recsys.recommendation import menu_recommendation
from functools import reduce
import datetime
import pandas as pd
from django.shortcuts import HttpResponse, redirect
from django.db.models import Q
from django.views.generic import View
from django.core.paginator import Paginator


# ログイン前ホーム画面
def home(request):
    pass


# ログイン・サインアップ関連
# サインアップ
def signup(request):
    pass


# ログイン
def login(request):
    pass

# ログアウト
def logout(request):
    pass


# ユーザホーム
def user_home(request):
    return render(request, 'pages/user_home.html')


def user_info_input(request):
    pass


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
    user_allergen = [User.allergen_choices[int(i)-1][1] for i in User.objects.get(id=user_id).allergen]
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


# カメラページ
# ストリーミング画像・映像を表示するview
class Camera(View):
    def get(self, request):
        return render(request, 'pages/camera.html', {})


# 撮った写真を表示
def lunch_photo(request):
    # Base64エンコードされた画像データ取得
    image = request.POST.get('image')
    print(image[:20])
    return render(request,
                  'pages/lunch_photo.html',
                  {'image': image})
