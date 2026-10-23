from django.shortcuts import render
from .models import Course

def course_planner(request):
    # 抓取資料庫裡所有的課程
    all_courses = Course.objects.all()
    # 資料打包傳給 index.html
    return render(request, 'index.html', {'courses': all_courses})