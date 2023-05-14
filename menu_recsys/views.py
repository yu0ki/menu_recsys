from django.shortcuts import render
from menu_recsys.models import User
from menu_recsys.database_update import database_update
from menu_recsys.models import Menu
from .order_recognition.image_processors import object_detect
from django.http import HttpResponse
import urllib
from django.shortcuts import get_object_or_404


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
    ctx = {
        "weather": "晴れ"
    }
    return render(request, 'pages/user_home.html', ctx)


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
    while dish_id is not None:
        dish_name = get_object_or_404(Menu, id=dish_id).dish_name
        dishes.append(dish_name)
        dish_id = request.POST.get('dish-' + str(len(dishes)))

    # TODO: データベースに保存
    
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
