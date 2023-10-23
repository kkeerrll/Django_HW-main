from django.urls import path
from . import views
from .views import (
    BlogPostListView,
    BlogPostDetailView,
    BlogPostCreateView,
    BlogPostUpdateView,
    BlogPostDeleteView,
    ArticleDetailView,
    ArticleListView,
    ArticleCreateView,
    ArticleEditView,
)
from .views import ProductListView, ProductCreateView, ProductDetailView
from userapp.views import register


urlpatterns = [
    path('products/<int:product_id>/', views.show_product, name='show_product'),
    path('', BlogPostListView.as_view(), name='blogpost-list'),
    path('<int:pk>/', BlogPostDetailView.as_view(), name='blogpost-detail'),
    path('create/', BlogPostCreateView.as_view(), name='blogpost-create'),
    path('<int:pk>/update/', BlogPostUpdateView.as_view(), name='blogpost-update'),
    path('<int:pk>/delete/', BlogPostDeleteView.as_view(), name='blogpost-delete'),
    path('article/<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
    path('articles/', ArticleListView.as_view(), name='article-list'),
    path('article/create/', ArticleCreateView.as_view(), name='article-create'),
    path('article/edit/<slug:slug>/', ArticleEditView.as_view(), name='article-edit'),
    path('products/', views.product_list, name='product_list'),
    path('versions/create/', views.create_version, name='create_version'),
    path('', ProductListView.as_view(), name='product-list'),
    path('create/', ProductCreateView.as_view(), name='product-create'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('register/', register, name='register'),



]