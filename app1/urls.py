from app1.views import *
from django.urls import path

app_name='hardwork'

urlpatterns=[
    path('data_render/', data_render, name= 'data_render'),
]