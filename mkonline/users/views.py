# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.backends import ModelBackend
from .models import UserProfile
from django.db.models import Q
from django.views.generic.base import View
from .forms import LoginForm,RegisterForm
from django.contrib.auth.hashers import make_password
from  utils.email_send import send_register_email
from .models import EmailVerfiyRecord


# 自定义验证模式
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user=UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None
# 注册视图
class RegisterView(View):
    def get(self,request):
        register_form=RegisterForm()
        return render(request,'register.html',{'register_form':register_form})
    def post(self,request):
        register_form=RegisterForm(request.POST)
        if register_form.is_valid():
            user_name=request.POST.get("username","")
#            if UserProfile.objects.filter(email=user_name):
#                return render(request, 'register.html', {'register_form': register_form,"msg":"邮箱已经注册"})
            password=request.POST.get("password","")
            user_profile=UserProfile()
            user_profile.username=user_name
            user_profile.email=user_name
            user_profile.password=make_password(password)
            user_profile.save()
            send_register_email(user_name,send_type="register")
            return render(request,"login.html")
        else:
            register_form=RegisterForm()
            return render(request, 'register.html', {'register_form': register_form})
# 激活视图
class AciveUserView(View):
    def get(self,request,active_code):
        all_recodes=EmailVerfiyRecord.objects.filter(code=active_code)
        if all_recodes:
            for recode in all_recodes:
                email=recode.email
                user=UserProfile.objects.get(email=email)
                user.is_active=True
                user.save()
        return render(request,"login.html")

#登录视图
class LoginView(View):
    def get(self,request):
        return render(request, "login.html", {})
    def post(self,request):
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            # 发起验证 用户名和密码是否正确
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, "index.html")
                else:
                    return render(request, "login.html", {"msg": "用户没有激活"})
            else:
                return render(request, "login.html", {"msg": "用户名或者密码错误"})
        else:
            login_form=LoginForm()
            return render(request,"login.html",{"login_form":login_form})






# Create your views here.
#def user_login(request):
#    if request.method=="POST":
#        user_name=request.POST.get("username","")
#        pass_word=request.POST.get("password","")
#        # 发起验证 用户名和密码是否正确
#        user=authenticate(username=user_name,password=pass_word)
#        if user is not None:
#            login(request,user)
#            return render(request,"index.html")
#        else:
#            return render(request,"login.html",{"msg":"用户名和密码错误"})

#   elif request.method=="GET":
#        return render(request,"login.html",{})
