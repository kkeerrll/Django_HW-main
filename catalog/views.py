from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Product
from django.utils.text import slugify



class HomeView(View):
    def get(self, request):
        # Логика и код представления
        return render(request, 'home.html')


class CreateProductView(View):
    def get(self, request):
        # Логика рендеринга формы создания товара
        return render(request, 'create_product.html')

    def post(self, request):
        # Логика обработки формы и создания товара
        return redirect('product-list')


class UpdateProductView(View):
    def get(self, request, product_id):
        product = Product.objects.get(id=product_id)
        # Логика рендеринга формы обновления товара
        return render(request, 'update_product.html', {'product': product})

    def post(self, request, product_id):
        product = Product.objects.get(id=product_id)
        # Логика обновления товара
        return redirect('product-list')

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import BlogPost

class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blogpost_list.html'
    context_object_name = 'blogposts'

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blogpost_detail.html'
    context_object_name = 'blogpost'

class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'blogpost_form.html'
    fields = ['title', 'slug', 'content', 'preview', 'is_published']
    success_url = reverse_lazy('blogpost-list')

class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blogpost_form.html'
    fields = ['title', 'slug', 'content', 'preview', 'is_published']
    context_object_name = 'blogpost'
    success_url = reverse_lazy('blogpost-list')

class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blogpost_confirm_delete.html'
    context_object_name = 'blogpost'
    success_url = reverse_lazy('blogpost-list')



class ArticleDetailView(View):
    def get(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        article.views += 1  # Увеличение счетчика просмотров
        article.save()
        return render(request, 'article_detail.html', {'article': article})

class ArticleListView(View):
    def get(self, request):
        articles = Article.objects.filter(published=True)  # Фильтрация только опубликованных статей
        return render(request, 'article_list.html', {'articles': articles})


class ArticleCreateView(View):
    def get(self, request):
        return render(request, 'article_create.html')

    def post(self, request):
        title = request.POST.get('title')
        content = request.POST.get('content')

        # Формирование slug-названия из заголовка
        slug = slugify(title)

        article = Article.objects.create(
            title=title,
            content=content,
            slug=slug,
            published=False
        )
        return redirect('article_detail', slug=article.slug)


class ArticleEditView(View):
    def get(self, request, slug):
        article = Article.objects.get(slug=slug)
        return render(request, 'article_edit.html', {'article': article})

    def post(self, request, slug):
        article = Article.objects.get(slug=slug)
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()

        # Формирование URL для просмотра отредактированной статьи
        redirect_url = '/article/{}'.format(slug)

        return redirect(redirect_url)
