from app2.views import *
from django.urls import *

app_name= 'luck'

urlpatterns=[
    path('data/', data, name= 'data'),
]