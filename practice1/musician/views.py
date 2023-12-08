from django.shortcuts import render, redirect
from . import forms
from . import models

def musician_list(request):
    musician_form = forms.MusicianForm()
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('musician_list')
        else:
            musician_form = forms.MusicianForm()
    return render(request, 'musician/musician.html', {'form1': musician_form})


def edit_musician(request, id_no):
    musician = models.Musician.objects.get(pk=id_no)
    musician_form = forms.MusicianForm(instance=musician)
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST, instance=musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('home')

    return render(request, 'musician/musician.html', {'form1': musician_form})
