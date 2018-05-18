from django.contrib.auth.decorators import login_required
from . import views
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   
    url(r'^$', views.index, name='index'),
    url(r'^music/$', views.music, name='music'),
    url(r'^upload/$', views.upload_file, name='upload'),
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
