from django.shortcuts import render, redirect
from articles.models import Article, Comment
from articles.forms import CommentForm
from django.contrib.auth.decorators import login_required
import random
# Create your views here.

@login_required
def HomePageView(request):
    # Llamamos a todos los artículos
    articles = Article.objects.all()
    
    # Seleccionar artículos aleatorios si existen
    if articles.exists():
        random_articles = list(articles)
        random.shuffle(random_articles)
        random_articles = random_articles[:5]
    else:
        random_articles = []  # Si no hay artículos, devolver lista vacía

    print("Artículos aleatorios seleccionados:", random_articles)  # Debug en consola
    
    # Formulario de comentarios
    form = CommentForm()
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            article_id = request.POST.get("article_id")
            comment.article = Article.objects.get(id=article_id)
            comment.author = request.user
            comment.save()
            return redirect("home")

    # 🔥 Agregamos random_articles al contexto 🔥
    return render(request, "home.html", {
        'articles': articles,
        'random_articles': random_articles,  # ✅ Ahora estará disponible en la plantilla
        'form': form
    })