# 　ユーザ身分確認

from django.shortcuts import redirect
from django.shortcuts import render


def user_account_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        user_account = kwargs.get('user_account')
        if request.user.is_authenticated and request.user.user_account == user_account:
            return view_func(request, *args, **kwargs)
        else:
            return render(request, "pages/dame.html")

    return _wrapped_view
