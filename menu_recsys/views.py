from django.shortcuts import render
from menu_recsys.models import User, Menu, Canteen
from menu_recsys.database_update import database_update
from functools import reduce
from django.shortcuts import HttpResponse, redirect
from django.db.models import Q
from django.views.generic import View

# ログイン前ホーム画面
def home(request):
    pass


# ログイン・サインアップ関連
# サインアップ
def signup(request):
    if request.method == "GET":
        return render(request, "pages/signup.html")
    user_account = request.POST.get("user_account")
    user_pwd = request.POST.get("user_pwd")
    if not User.objects.filter(user_account=user_account).exists():
        User.objects.create(user_account=user_account, user_pwd=user_pwd)
        return render(request, "pages/user_home.html", {"msg": "Account created successfully"})
    else:
        return render(request, "pages/signup.html", {"error_msg": "username existed!"})


# ログイン
def login(request):
    if request.method == "GET":
        return render(request, "pages/login.html")

    user_account = request.POST.get("user_account")
    user_pwd = request.POST.get("user_pwd")
    if User.objects.filter(user_account=user_account).exists():
        user_existed = User.objects.get(user_account=user_account)
        if user_existed.user_pwd == user_pwd:
            return render(request, "pages/user_home.html", {"msg": "Login successfully"})
        else:
            return render(request, "pages/login.html", {"error_msg": "Incorrect password"})
    else:
        return render(request, "pages/login.html", {"error_msg": "Incorrect account"})


# ログアウト
def logout(request):
    pass


# ユーザホーム
def user_home(request):
    return render(request, 'pages/user_home.html')


def user_info_input(request):
    pass


# 検索条件入力
def search(request):
    if request.method == "GET":
        context = {
            "canteen_name_choices": Canteen.canteen_name_choices,
        }
        return render(request, "pages/search.html", context=context)
    budget = request.POST.get("budget")
    canteen = request.POST.get("canteen")
    types = request.POST.get("types")
    target = request.POST.get("target")
    # function: searching suitable menu returns menu ids
    menu_id = [325, 326, 327, budget]
    return recommend(request, menu_id=menu_id)

    # x = database_update.canteen_database_update()
    # if x:
    #     return render(request, "pages/recommend.html")
    # else:
    #     return render(request, "pages/search.html")


# 検索結果
def recommend(request, menu_id=None):
    if menu_id is None:
        menu = Menu.objects.all()
    else:
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