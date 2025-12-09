from django.urls import path
from . import views

urlpatterns = [
    path('noticias/', views.Noticias, name='lista_noticias'),
    path('noticias/<int:pk>/', views.DetailNoticiasView.as_view(), name='detalhe_noticias'),
]