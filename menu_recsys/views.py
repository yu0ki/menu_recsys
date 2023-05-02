from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse

def my_view(request):
    # Do some work here...
    return HttpResponse("Hello, world!")



# ログイン前ホーム画面
def home(request):
    pass


# ログイン・サインアップ関連
# サインアップ
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("https://www.baidu.com")
    else:
        form = UserCreationForm()
    return render(request, "pages/signup.html", {"form": form})
    pass


# ログイン
def login(request, user):
    pass


# ログアウト
def logout(request):
    pass


# ユーザホーム
def user_home(request):
    return render(request, 'pages/user_home.html')


# 検索条件入力
def search(request):
    pass


# 検索結果
def recommend(request):
    pass
