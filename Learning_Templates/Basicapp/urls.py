
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'Basicapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('other/', views.other, name='other'),
    path('relative_templates/', views.relative_templates, name='relative_templates'),
    path('base/', views.base, name='base'),

]