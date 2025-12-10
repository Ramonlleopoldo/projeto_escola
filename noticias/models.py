import html
from django.db import models
from django.utils.html import strip_tags


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=300)

    def __str__(self):
        return self.nome


class Noticia(models.Model):
    id = models.AutoField(primary_key=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="noticia_categoria"
    )
    titulo = models.CharField(max_length=300)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    capa = models.ImageField(upload_to="noticias/capa", blank=True, null=True)

    @property
    def breve_descricao(self):
        # Remove as tags HTML (<p>, <b>, etc)
        texto_sem_tags = strip_tags(self.descricao)
        
        # Converte entidades (&nbsp; vira espaço, &amp; vira &, etc)
        texto_limpo = html.unescape(texto_sem_tags)
        
        # Remove espaços extras e quebras de linha suja
        texto_final = " ".join(texto_limpo.split())

        if len(texto_final) <= 100:
            return texto_final
        else:
            return texto_final[:100].rsplit(" ", 1)[0] + "..."

    class Meta:
        ordering = ["-data_criacao"]

    def __str__(self):
        return self.titulo


class ImagemNoticia(models.Model):
    id = models.AutoField(primary_key=True)
    noticia = models.ForeignKey(
        Noticia, on_delete=models.CASCADE, related_name="imagens"
    )
    arquivo = models.ImageField(upload_to='noticias')
