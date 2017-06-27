#coding:utf-8
from  django import  forms
from captcha.fields import CaptchaField
class LoginForm(forms.Form):
    username=forms.CharField(required=True,max_length=50)
    password=forms.CharField(required=True,max_length=50)


class RegisterForm(forms.Form):
    username=forms.EmailField(required=True)
    password=forms.CharField(required=True,max_length=50)
    captcha = CaptchaField()
