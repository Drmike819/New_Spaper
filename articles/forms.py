from django import forms

from .models import Comment, Article, ArticleImage
from django.forms import inlineformset_factory

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        
# formulario de que permite actualizar los articulos
class ArticleForm(forms.ModelForm):
    class Meta:
        # indeca que el formulario se base en el modelo(tabla) article
        model = Article
        # indica los campos que se incluiran en el formulario
        fields = ['title', 'body',]

# permite crear varios formularios que es util para manejar modelos relacionados
ArticleImageFormSet = inlineformset_factory(
    # modelo al que esta asociado las imagenes
    Article,
    # modelo que contiene la relacion
    ArticleImage,
    # campo del formulario
    fields=['image'],
    # Indica que se mostrará un formulario vacío adicional para añadir una nueva imagen.
    extra=1,
    #opcion para eliminar una imagen de un articulo
    can_delete=True
)