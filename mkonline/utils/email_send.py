#coding:utf-8
from users.models import EmailVerfiyRecord
import random
from django.core.mail import send_mail
from mkonline.settings import EMAIL_FROM
# 生成随机密码的方法
def random_str(randomlength=8):
    str=""
    chars="AaBcAeRdWEdRtrbhttokdqssDeqholplLpu=PWQIEETXAQQRTMDJQRsbmwxtydspews0123456789"
    length=len(chars)-1
    for i in range(randomlength):
        str+=chars[random.randint(0,length)]
    return str
def send_register_email(email,send_type="register"):
    email_record=EmailVerfiyRecord()
    code=random_str(16)
    email_record.code=code
    email_record.email=email
    email_record.send_type=send_type
    email_record.save()
    if send_type=="register":
        email_title="慕学在线网注册激活链接 "
        email_body="请你点击下面的链接激活你的账号：http://127.0.0.1:8000/active/{0}".format(code)

        send_status=send_mail(email_title,email_body,EMAIL_FROM,[email])
        if send_status:
            pass















