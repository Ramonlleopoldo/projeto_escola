from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from . import models


def Noticias(request):
    noticias = models.Noticia.objects.all()
    print(f"Essa é a noticia {noticias}")

    return render(request, "noticias.html", {"noticias": noticias})


class DetailNoticiasView(DetailView):
    model = models.Noticia
    template_name = "noticias_detalhes.html"

