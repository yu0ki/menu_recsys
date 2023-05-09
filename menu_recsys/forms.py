
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth.forms import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['user_account']
        labels = {
            'user_account': 'アカウント名（必須)'
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_name', 'user_email', 'age', 'height', 'weight', 'gender', 'target']
        labels = {
            'user_email': 'メールアドレス',
            'user_name': 'ニックネーム(必須)',
            'age': '年齢',
            'height': '身長(cm)',
            'weight': '体重(kg)',
            'gender': '性別（default:田佬）',
            'target': '目標',
        }

