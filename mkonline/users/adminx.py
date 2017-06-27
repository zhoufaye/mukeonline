#from django.contrib import admin
#coding:utf-8
# Register your models here.
import xadmin
from .models import *
from xadmin import views

#class UserProfileAdmin(object):
#    list_display=["nick_name","birday","gender","address","moblie","image"]
#    search_fields=["nick_name","birday","gender","address","moblie"]
#    list_filter=["nick_name","birday","gender","address","moblie","image"]

class BaseSetting(object):
    enable_themes=True
    use_bootswatch=True

class GlobalSetting(object):
    site_title="慕学管理系统"
    site_footer="慕学在线网"
    menu_style="accordion"


class EmailVerfiyRecordAdmin(object):
    list_display=["code","email","send_type","send_time"]
    search_fields=["code","email","send_type"]
    list_filter=["code","email","send_type","send_time"]


class BannerAdmin(object):
    list_display=["title","image","url","index","add_time"]
    search_fields=["title","url","index"]
    list_filter=["title","image","url","index","add_time"]

#xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(EmailVerfiyRecord,EmailVerfiyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSetting)






