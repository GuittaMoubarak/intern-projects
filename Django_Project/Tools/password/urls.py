from django.urls import path, include
from . import views
app_name = 'password'
urlpatterns = [
    path('', views.index, name='index'),
    path('remove/<int:id>', views.remove, name="remove"),
    path('Add/', views.Add, name="Add"),
]
