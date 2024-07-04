from django.contrib import admin
# from . models import User_signin
from django.contrib.auth.admin import UserAdmin
from . models import MyUser,StayPics,DinePics

# from django.contrib.gis.admin import OSMGeoAdmin

# Register your models here.

admin.site.register(MyUser)
admin.site.register(StayPics)
admin.site.register(DinePics)