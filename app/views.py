from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import course
from .decorators import unauthenticated_user_courses
# Create your views here.


def index(request):
    data = course.objects.all()
    context = {
        "data" : data,
    }
    return render(request, "index.html", context)

def particular(request):
    return render(request, "particularCourse.html")

@unauthenticated_user_courses
def eachdetail(request, title):
    each = course.objects.get(course_name = title)
    context = {
        "each" : each,
    }
    return render(request, "particularCourse.html" , context)