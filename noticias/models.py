from django.db import models


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
        texto = self.descricao
        if len(texto) <= 100:
            return texto
        else:
            corte = texto[:100]
        # Corta no último espaço para não quebrar palavra
        return corte.rsplit(" ", 1)[0] + "..."

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
