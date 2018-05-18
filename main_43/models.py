from django.db import models

# Create your models here.

class Music(models.Model):
    """Музыка"""
    name = models.TextField()
    url = models.TextField()
    genre = models.TextField()
    file = models.FileField()
    
    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.name