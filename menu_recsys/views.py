from django.shortcuts import render
from menu_recsys.models import User


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
    pass

# 検索結果
def recommend(request):
    pass
