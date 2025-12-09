from django.contrib import admin
from . import models


class ImagemProdutoInline(admin.TabularInline):
    model = models.ImagemNoticia
    extra = 1  # Quantos campos de upload vazios aparecem por padrão

class CategoriaAdmin(admin.ModelAdmin):
    list_display = (
        "nome",
    )
    search_fields = ("nome",)


class NoticiasAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "descricao",
    )
    inlines = [
        ImagemProdutoInline,
    ]
    search_fields = ("titulo",)


admin.site.register(models.Categoria, CategoriaAdmin)
admin.site.register(models.Noticia, NoticiasAdmin)
