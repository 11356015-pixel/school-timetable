from django.shortcuts import render
from .models import Course

def course_planner(request):
    all_courses = Course.objects.all()
    return render(request, 'index.html', {'courses': all_courses})