from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('<int:news_id>/', views.news_detail, name='news_detail'),
    re_path('^register/$', views.RegisterFormView.as_view()),
    re_path('^login/$', views.LoginFormView.as_view()),
    re_path('^logout/$', views.LogoutView.as_view()),
    re_path('^password-change/', views.PasswordChangeView.as_view())
]