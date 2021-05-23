from django.urls import path
from RevisedApp import views
from django.contrib.auth import views as ad  

urlpatterns=[
path('',views.homepage,name='home'),
path('abt/',views.abtpage,name='about'),
path('ach/',views.ach,name='ach'),
path('lg/',ad.LoginView.as_view(template_name="html/login.html"),name='log'),
path('lgout/',ad.LogoutView.as_view(template_name="html/logout.html"),name='logo'),
path('reg/',views.register,name='reges'),
path('rol/',views.role,name='main'),
path('req/',views.requestform,name='request'),
path('per/',views.permissions,name='perm'),
path('eper/<int:k>/',views.gvper,name='gp'),
path('das/',views.dashboard,name='dash'),
path('jobs/',views.jobposts,name='job'),
path('ejobs/<int:a>/',views.editjobs,name='editjob'),
path('updf/',views.updf,name='update'),
path('pro/',views.profile,name='profile'),
path('ch/',views.cgf,name='cg'),
path('rst/',ad.PasswordResetView.as_view(template_name='html/resetpassword.html'),name='reset_password'),
path('rst_done/',ad.PasswordResetDoneView.as_view(template_name='html/resetpassworddone.html'),name="password_reset_done"),
path('rst_confirm/<uidb64>/<token>/',ad.PasswordResetConfirmView.as_view(template_name='html/resetpasswordconfirm.html'),name='password_reset_confirm'),
path('rst_cmplt/',ad.PasswordResetCompleteView.as_view(template_name='html/reset_password_complete.html'),name="password_reset_complete"),
path('viewjob/',views.viewjob,name='view'),
path('jobinfo/',views.jobinfo,name='jinfo'),
path('studinfo/',views.studentinfo,name='stdinfo'),
]