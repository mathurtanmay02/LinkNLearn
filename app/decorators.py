from django.shortcuts import redirect,render
from django.http import HttpResponse

def unauthenticated_user_courses(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('app:index')

    return wrapper_func