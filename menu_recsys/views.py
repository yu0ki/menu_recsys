from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
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
            return redirect("../login/")
    else:
        form = UserCreationForm()
    return render(request, "pages/signup.html", {"form": form})
    pass


# ログイン
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('https://www.yahoo.com')
    else:
        form = AuthenticationForm()
    return render(request, "pages/login.html", {"form": form})
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
