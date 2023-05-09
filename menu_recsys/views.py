from django.shortcuts import render

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
        "weather": "sunny"
    }
    return render(request, 'pages/user_home.html', ctx)


# 検索条件入力
def search(request):
    pass


# 検索結果
def recommend(request):
    pass
