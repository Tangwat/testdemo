from django.urls import path, include
from .import views

app_name = 'demoapp'
urlpatterns=[
   path('', views.index, name='index'),
]