
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url

from . import views


urlpatterns = [
    path('', views.book, name='book'),
    url(r'^(?P<book_id>[0-9]+)/$', views.detail, name='detail')
]
