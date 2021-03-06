"""ManytoManyRelationsproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showIndex,name="main"),
    path('add_course/', views.addCourse,name="add_course"),
    path('save_course/', views.save_course,name="save_course"),
    path('view_course/', views.view_course,name="view_course"),
    path('add_student/', views.add_student,name="add_student"),
    path('save_student/',views.save_student,name="save_student"),
    path('view_student/', views.view_student,name="view_student"),
]
