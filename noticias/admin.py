from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from . import models


class ImagemProdutoInline(admin.TabularInline):
    model = models.ImagemNoticia
    extra = 1  # Quantos campos de upload vazios aparecem por padrão


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)


class NoticiasAdmin(SummernoteModelAdmin):
    summernote_fields = ("descricao",)

    inlines = [
        ImagemProdutoInline,
    ]
    search_fields = ("titulo",)


admin.site.register(models.Categoria, CategoriaAdmin)
admin.site.register(models.Noticia, NoticiasAdmin)
