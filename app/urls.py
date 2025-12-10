from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contatos/', views.Contato, name='contatos_list'),
    path('', include('noticias.urls')),
    path('summernote/', include('django_summernote.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
