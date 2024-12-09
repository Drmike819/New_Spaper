from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # Relación en donde un articulo puede tener varias imagenes
    article_images = models.ManyToManyField('ArticleImage', related_name='articles_related', blank=True)  # Cambio a 'articles_related'
    # Relación con el autor
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # Función que crea una URL en base al nombre de la vista
    def get_absolute_url(self):
        return reverse("home")


# modelo que para las imagenes de los articulos
class ArticleImage(models.Model):
    #conexion de muchos a uno (muchas imagenes pueden estar en un articulo)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_images_related')  # Modificar a 'article_images_related'
    image = models.ImageField(upload_to='article_images/')
    #almacena una fecha de creacion
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.article.title}"


    
    
#creamos una base para lo comentarios
class Comment(models.Model):
    # indicamos que a la hora de eliminar el articulo este comentario se eliminara
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.CharField(max_length=140)
    # indiacamos que el autor del articulo es el usuario personalizado
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse('article_list')