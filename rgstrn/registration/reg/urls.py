from django.contrib import admin
from django.urls import path
from.import views
from django.conf.urls import url
urlpatterns = [

url('/', views.register, name='register')

]