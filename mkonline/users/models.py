# coding:utf-8
from django.db import models
from  django.contrib.auth.models import  AbstractUser
# Create your models here.
from datetime import  datetime
class UserProfile(AbstractUser):
    gender_choice=(
        ("male","男"),
        ("female","女"),
    )
    nick_name=models.CharField(max_length=100,verbose_name="昵称")
    birday=models.DateTimeField(verbose_name="生日",null=True,blank=True)
    gender=models.CharField(choices=gender_choice,default="female",max_length=30)
    address=models.CharField(max_length=100)
    mobile=models.CharField(max_length=11,null=True,blank=True)
    image=models.ImageField(upload_to="image/%Y/%m",default="image/default.png")
    class Meta:
        verbose_name="用户信息"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.username

class EmailVerfiyRecord(models.Model):
    code=models.CharField(max_length=20,verbose_name="验证码")
    email=models.EmailField(max_length=50,verbose_name="邮箱")
    send_type=models.CharField(choices=(("register","注册"),("forget","找回密码")),max_length=50)
    send_time=models.DateTimeField(default=datetime.now)
    class Meta:
        verbose_name="邮箱验证码"
        verbose_name_plural=verbose_name
class Banner(models.Model):
    title=models.CharField(max_length=100,verbose_name="标题")
    image=models.ImageField(upload_to="banner/%Y/%m",verbose_name="轮播图",max_length=100)
    url=models.URLField(max_length=200,verbose_name="访问地址")
    index=models.IntegerField(default=100,verbose_name="顺序")
    add_time=models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name="轮播图"
        verbose_name_plural=verbose_name









