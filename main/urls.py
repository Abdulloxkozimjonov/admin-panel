from django.urls import path
from . import views

urlpatterns = [
    path('create_xaridor/', views.create_xaridorlar_view, name='create_xaridorlar_url'),
    path('index/', views.dashboard_page_view, name='index_url'),
    path('', views.login_view, name='login_url'),
    path('register/', views.register_view, name='register_url'),
    path('home/', views.home_view, name='home_url'),
    path('home2/', views.home2_view, name='home2_url'),
    path('sign_out/', views.log_out, name='sigin_out'),
]