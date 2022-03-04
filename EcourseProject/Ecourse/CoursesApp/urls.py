import ckeditor_uploader
from django.contrib import admin
from django.urls import path, include, re_path
from . import  views
import ckeditor_uploader
from rest_framework import routers

r = routers.DefaultRouter()
r.register('course', views.CourseViewSet)

urlpatterns = [
    path('', include(r.urls)),
    re_path(r'^ckeditor/',include('ckeditor_uploader.urls')),

]
