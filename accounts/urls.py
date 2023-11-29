from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'), #ログインページのビュー
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'), #ログアウトページのビュー
    path('signup/',views.SignUpView.as_view(),name='signup'), #新規登録ページのビュー
    path('signup_success/',views.SignUpSuccessView.as_view(),name='signup_success'), #新規登録完了ページのビュー
]
