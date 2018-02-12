from django.urls import path, include
from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'api/list', views.get_rest_list, name='get_rest_list'),
]
