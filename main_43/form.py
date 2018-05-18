from django import forms

from .models import Music


    
class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['name', 'url', 'genre','file']
        labels = {'name': 'Название','url' : 'Пока не заполнять', 'genre' : 'Жанр', 'file' : 'Песня'}

