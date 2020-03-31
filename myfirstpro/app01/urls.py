from django.urls import path
from . import views

urlpatterns=[
    path('',views.add_book,name='add_book'),
    # 如果想在add_book下面再加模块直接写上就行one,views下再加个方法就行。
    path('one',views.add_one,name='one'),
]