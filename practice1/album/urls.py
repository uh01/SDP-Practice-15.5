# album/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.album_list, name='album_list'),
    path('edit/<int:id_no>/', views.edit_album, name='edit_album'),
    path('delete/<int:id_no>', views.detete_entry, name='delete_entry'),
]