from django.urls import path, include
from . import views
app_name = 'converter'
urlpatterns = [
        path('', views.index, name='index'),
]