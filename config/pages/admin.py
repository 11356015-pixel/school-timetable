from django.contrib import admin
from .models import Course

# 將 Course 註冊到管理後台
admin.site.register(Course)
