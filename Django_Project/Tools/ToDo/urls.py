from django.urls import path, include
from . import views
app_name = 'ToDo'
urlpatterns = [
    path('', views.index, name='index'),
    path('check/<int:id>', views.check, name="check"),
      path('remove/<int:id>', views.remove, name="remove"),
]
