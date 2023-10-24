from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Product
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import BlogPost
from django.shortcuts import render
from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404



def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


class HomeView(View):
    def get(self, request):
        # Логика и код представления
        return render(request, 'home.html')

class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    # Переопределение метода get_queryset, чтобы отображать только продукты текущего пользователя
    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name']
    # Переопределение метода form_valid, чтобы автоматически привязать продукт к пользователю
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    # Переопределение метода get_queryset, чтобы отображать только продукты текущего пользователя
    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)


class CreateProductView(View):
    def get(self, request):
        # Логика рендеринга формы создания товара
        return render(request, 'create_product.html')

    def post(self, request):
        # Логика обработки формы и создания товара
        return redirect('product-list')


class UpdateProductView(View):

    def edit_product(request, product_id):
        product = get_object_or_404(Product, pk=product_id)

        # Проверка, является ли текущий пользователь владельцем продукта
        if request.user != product.owner:
            return HttpResponseForbidden("Вы не являетесь владельцем этого продукта")

        if request.method == 'POST':
            # Обработка формы редактирования продукта
            def post(self, request, product_id):
                product = Product.objects.get(id=product_id)
                # Логика обновления товара
                return redirect('product-list')

        else:
            # Отображение формы редактирования
            def get(self, request, product_id):
                product = Product.objects.get(id=product_id)
                # Логика рендеринга формы обновления товара
                return render(request, 'update_product.html', {'product': product})





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
