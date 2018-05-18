from django.shortcuts import render
from django.http import HttpResponseRedirect

from .form import UploadFileForm
from .models import Music

# Create your views here.

def index(request):
    """Главная страница 43"""
    return render(request, 'main_43/index.html')

def music(request):
    """Выводит список тем."""
    music = Music.objects.all()
   
    context = {'music': music }
    
    return render(request, 'main_43/the_music.html', context)


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            
            instance = Music(file = request.FILES['file'])
            instance = form.save()
            return HttpResponseRedirect('../music')
    else:
        form = UploadFileForm()
    return render(request, 'main_43/upload.html', {'form': form})