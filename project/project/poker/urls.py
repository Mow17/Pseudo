import django.contrib.auth.views
from django.urls import path,include
from . import views
from django.conf.urls import url

app_name='poker'

urlpatterns=[
    path('top/',views.top_page, name="top"),
]
