from django.urls import path
from CRT import views
from django.contrib.auth import views as ad

urlpatterns=[
path('',views.home,name='hm'),
path('achiev/',views.achievment,name='ach'),
path('user/',views.loginpage,name='log'),
path('progress/',views.progress_page,name='ph'),
]
