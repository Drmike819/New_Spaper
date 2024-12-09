from django.contrib import admin
from .models import Article, Comment

# Register your models here.

#sirve para el diseño del como se vera en el administrador
class CommentInline(admin.StackedInline):
    model = Comment
    Extra = 0
 
#indicamos que los campos creados en articles/models.py apareceran en el administrador de django    
class ArticleAdmin(admin.ModelAdmin):
    inlines =[
        CommentInline,
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)