from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

from menu_recsys.forms import SignUpForm, UserProfileForm, UserAllergenForm
from django.contrib import messages
from menu_recsys.models import User, History_order
from .decorators import user_account_required


def my_view(request):
    # Do some work here...
    return HttpResponse("Hello, world!")

from menu_recsys.models import User
from menu_recsys.database_update import database_update
from menu_recsys.models import Menu
from .order_recognition.image_processors import object_detect
from django.http import HttpResponse
import urllib
from django.shortcuts import get_object_or_404


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
    return render(request, "pages/user_home.html", {"user": user, "weather": "晴れ"})


def user_info_input(request):
    pass


# 検索条件入力
def search(request):
    pass
    # x = database_update.canteen_database_update()
    # if x:
    #     return render(request, "pages/recommend.html")
    # else:
    #     return render(request, "pages/search.html")


# 検索結果
def recommend(request):
    pass


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


    
    # # SNSシェア用リンク
    # hashtag = "#PlatePandA"
    # url = f"https://twitter.com/intent/tweet?text={urllib.parse.quote(hashtag)}&url=&hashtags={urllib.parse.quote(hashtag)}&amp;media={urllib.parse.quote(base64_image)}"

    # renderでそれっぽい画面を返す
    return render(request, 
                  'pages/submit_lunch.html', 
                  {'image': base64_image,
                   "detected_dish_info": dishes,
                #    "twitter_share_url": url
                   })


def update_menu_database(request):
    # データ更新
    database_update.canteen_database_update()
    return HttpResponse("Updating menu database was finished!")
