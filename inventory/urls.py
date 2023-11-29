from django.urls import path
from . import views

app_name = 'inventory'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'), #トップページのビュー
    path('post/',views.CreateInvView.as_view(),name='post'), #在庫登録機能のビュー指定
    path('post_done/',views.PostSuccessView.as_view(),name='post_done'), #在庫登録機能のビュー指定
    path('prev/',views.ReadingView.as_view(),name='reading'), #在庫閲覧機能のビュー指定
    path('contact/',views.ContactView.as_view(),name='contact'), #問い合わせ機能のビュー指定
]
