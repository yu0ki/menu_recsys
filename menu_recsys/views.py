from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from menu_recsys.forms import SignUpForm, UserProfileForm
from django.contrib import messages
from django import forms


def my_view(request):
    # Do some work here...
    return HttpResponse("Hello, world!")


# ログイン前ホーム画面
def home(request):
    return render(request, "pages/home.html",)
    pass


# ログイン・サインアップ関連
# サインアップ
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.add_message(request, messages.Sucess, "SUCCESS")
            return redirect("../login/")
    else:
        form = SignUpForm()
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
                return redirect('../user_home/')
    else:
        form = AuthenticationForm()
    return render(request, "pages/login.html", {"form": form})
    pass


# ログアウト
def logout(request):
    pass


# ユーザホーム
def user_home(request):
    # if request.method("POST"):
    #     return redirect('../profile')
    # return HttpResponse("Hello, world!")
    return render(request, 'pages/user_home.html')


# 検索条件入力
def search(request):
    pass


# 検索結果
def recommend(request):
    pass


def profile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("../user_home/")
    else:
        form = UserProfileForm()
    return render(request, "pages/profile.html", {"form": form})

    pass
