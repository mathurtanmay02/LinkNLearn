from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = "index"),
    path('particular', views.particular, name = "particular"),
    path('each/<str:title>/', views.eachdetail, name = "each"),
]