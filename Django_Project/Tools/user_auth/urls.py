from django.urls import path
from . import views
app_name = 'user_auth'
urlpatterns = [
    path('', views.user_login, name='index'),
    path('user_logout', views.user_logout, name="logout"),
    path('user_register', views.user_register, name="user_register"),

]