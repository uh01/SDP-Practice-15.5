# musician/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.musician_list, name='musician_list'),
    path('edit/<int:id_no>/', views.edit_musician, name='edit_musician'),
]

