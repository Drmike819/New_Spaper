from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from .models import Article, Comment
from .forms import CommentForm, ArticleImageFormSet, ArticleForm

# Create your views here.

# Vista para manejar la obtención de un artículo con el formulario de comentarios
class CommentGet(LoginRequiredMixin, DeleteView):
    model = Article
    template_name ="home.html"
    # Se pasa el formulario de comentarios al contexto
    def get_context_data(self, **Kwargs):
        context = super().get_context_data(**Kwargs)
        context['form'] = CommentForm()
        return context

# Vista para manejar el envío del formulario de comentarios
# Corregido: Se hereda de `FormView` y `SingleObjectMixin` para tener acceso a `get_object()`       
class CommentPost(LoginRequiredMixin, SingleObjectMixin, FormView):
    model = Article
    form_class = CommentForm
    template_name ="home.html"

    def post(self, request, *args, **kwargs):
        # Corregido: Usamos `self.get_object()` para obtener el artículo relacionado
        self.object = self.get_object(queryset=Article.objects.all())
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        # Guardamos el comentario sin comprometerlo a la base de datos aún
        comment = form.save(commit=False)
        # Asignamos el artículo al comentario
        comment.article = self.object
        comment.author = self.request.user
        # Guardamos el comentario
        comment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        # Redirige de nuevo al detalle del artículo después de guardar el comentario
        # return reverse('article_detail', kwargs={'pk': self.object.pk})
        return reverse('home')

# Vista que combina las operaciones GET y POST para el detalle de un artículo y la creación de comentarios      
class ArticleDetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        # Llamamos a la vista CommentGet para manejar la vista de detalles del artículo
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)
     # Llamamos a la vista CommentPost para manejar la creación de un comentario
    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)

# Vista para actualizar un artículo        
class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    # indica el modelo
    model = Article
    # formulario principal
    form_class = ArticleForm
    # template que se utilizara para esta vista
    template_name = "article_edit.html"

    # funcion que define el contexto(crear o editar)
    def get_context_data(self, **kwargs):
        # llama a la clase padre para obtner el contexto (ArticleUpdateView ArticleCreateView)
        data = super().get_context_data(**kwargs)
        # verifica si el metodo es HTTP POST lo cual asegura si el usuario esta enviando datos
        if self.request.POST:
            # crea un formulario de las imagenes y le paso datos envias como archivos enviados
            data['formset'] = ArticleImageFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            # si no es POST crea un formulario vacio para que el usuario suba sus imagenes
            data['formset'] = ArticleImageFormSet(instance=self.object)
        # devuelve el contexto y el formulario de las imagenes
        return data
    # metodo llamado cuando el formulario es valido
    def form_valid(self, form):
        # llamamos al contexto actual
        context = self.get_context_data()
        # se extrae el formulario del contexto
        formset = context['formset']
        # se verifica que si los formularios son validos
        if form.is_valid() and formset.is_valid():
            # Guarda el formulario principal en la base de datos
            self.object = form.save()
            # se asigna el formulario a la instanci
            formset.instance = self.object
            # se guarda el formulario
            formset.save()
            return redirect('home')  # Redirige al home después de una actualización exitosa
        else:
            # si no es valido se llama al meto el cual puede manejar errores
            return self.form_invalid(form)

    def get_success_url(self):
        # No es necesario definir un método get_success_url si estás usando 'redirect' en form_valid
        return reverse_lazy('home')  # Esto redirige al home si se usara el método 'get_success_url'

# Vista para eliminar un artículo
class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("home")
    # Verificación para asegurarse de que solo el autor pueda eliminar
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

# Vista para crear un nuevo artículo
class ArticleCreateView(LoginRequiredMixin, CreateView):
    # indicamos el modelo que se utilizara
    model = Article
    # indicamos el template el cual se utilizara
    template_name = 'article_new.html'
    # indicamos el formulario que vamos a utilizar
    form_class = ArticleForm

    # funcion que define el contexto(crear o editar)
    def get_context_data(self, **kwargs):
        # llama a la clase padre para obtner el contexto (ArticleUpdateView ArticleCreateView)
        data = super().get_context_data(**kwargs)
        # verifica que el metodo sea POST
        if self.request.POST:
            # si es POST Crea un formulario de las imagenes y le paso datos envias como archivos enviados
            data['formset'] = ArticleImageFormSet(self.request.POST, self.request.FILES)
        else:
            # si no es POST crea un formulario vacio para que el usuario suba sus imagenes
            data['formset'] = ArticleImageFormSet()
        return data

    # se llama la funcion cuando el formulario es valido
    def form_valid(self, form):
        # se asigna el author al formulario
        form.instance.author = self.request.user
        # llama a el contexto 
        context = self.get_context_data()
        #Extrae el formset del contexto
        formset = context['formset']
        # verifica si el formulario es valido
        if form.is_valid() and formset.is_valid():
            # Guarda el formulario principal en la base de datos
            self.object = form.save()
            #Asigna el objeto guardado (self.object) como la instancia relacionada para cada formulario
            formset.instance = self.object
            # Guarda el formset en la base de datos
            formset.save()
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)
    
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_edit.html'
    
    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user
    # redirige al template home
    def get_success_url(self):
        return reverse_lazy('home', kwargs={'pk':self.object.article.pk})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'comment_delete.html'
    
    # Este método asegura que solo el autor puede eliminar el comentario
    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user
    
    # redirige al template home
    def get_success_url(self):
        # Redirigir a la página del artículo después de eliminar el comentario
        return reverse_lazy('home', kwargs={'pk': self.object.article.pk})

# class ArticlesList(LoginRequiredMixin, ListView):
#     model = Article
#     template_name ='articles_list.html'