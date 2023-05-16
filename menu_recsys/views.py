from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

from menu_recsys.forms import SignUpForm, UserProfileForm, UserAllergenForm
from django.contrib import messages
from menu_recsys.models import User
from .decorators import user_account_required


def my_view(request):
    # Do some work here...
    return HttpResponse("Hello, world!")


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
    pass


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
    pass


# ログアウト
def logout_view(request):
    logout(request)
    return redirect("../login")


# 　ユーザ身分確認
# ユーザホーム
@user_account_required
def user_home(request, user_account):
    user = get_object_or_404(User, user_account=user_account)
    return render(request, "pages/user_home.html", {"user": user})


# 検索条件入力
def search(request):
    pass


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
