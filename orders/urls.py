from django.urls import path
from .views import *
from django.config,urls.static import static
urlpatterns = [
    
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)