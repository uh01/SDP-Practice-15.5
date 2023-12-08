# album/views.py
from django.shortcuts import render, redirect
from . import forms
from . import models

def album_list(request):
    album_form = forms.AlbumForm()
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('album_list')
        else:
            album_form = forms.AlbumForm()

    return render(request, 'album/album.html', {'form2': album_form})


def edit_album(request, id_no):
    album = models.Album.objects.get(pk=id_no)
    album_form = forms.AlbumForm(instance=album)
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST, instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('home')

    return render(request, 'album/album.html', {'form2': album_form})


def detete_entry(request, id_no):
    try:
        album = models.Album.objects.get(pk=id_no)
        album.delete()
        return redirect("home")
    except models.Album.DoesNotExist:
        return render(request, 'album/album_not_found.html', {'id_no': id_no})