from django.shortcuts import render
from django.views import View
import tweepy

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
    ctx = {
        "weather": "曇り時々",
        "max_temp": "28℃",
        "min_temp": "14℃",
        "panda_type": "nutral", #nutral, slim, muscleの3つ?
        "panda_status": "fine", #fine, notgood, fatの3つ?
    }
    return render(request, 'pages/user_home.html', ctx)


# 検索条件入力
def search(request):
    pass


# 検索結果
def recommend(request):
    pass


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
