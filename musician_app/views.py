from django.shortcuts import render, redirect
from . import forms
from . import models
# Create your views here.


def home(request):
    albums = models.Album.objects.all()
    return render(request, 'home.html', {'albums': albums})


def add_musician(request):
    if request.method == 'POST':
        form = forms.MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = forms.MusicianForm()
    return render(request, 'add_musician.html', {'form': form})


def add_album(request):
    if request.method == 'POST':
        form = forms.AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = forms.AlbumForm()
    return render(request, 'add_album.html', {'form': form})


def edit_musician(request, id):
    musician = models.Musician.objects.get(pk=id)
    form = forms.MusicianForm(instance=musician)
    if request.method == 'POST':
        form = forms.MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'edit_musician.html', {'form': form})


def edit_album(request, id):
    album = models.Album.objects.get(pk=id)
    musician_pk = album.musician.pk
    form = forms.AlbumForm(instance=album)
    if request.method == 'POST':
        form = forms.AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'edit_album.html', {'form': form, 'musician_pk': musician_pk})


def delete_album(request, id):
    album = models.Album.objects.get(pk=id)
    album.delete()
    return redirect('home')
