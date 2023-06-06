from django.urls import path, include
from . import views
app_name = 'weather'
urlpatterns = [
    path('', views.index, name='index'),
]