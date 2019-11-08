from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('sign', views.sign, name='sign'),
    path('log', views.log, name="log"),
    path('save', views.save, name="save"),
    ]