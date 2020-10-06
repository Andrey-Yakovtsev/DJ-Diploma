from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Article


def main_page(request):
    products = Product.objects.filter(available=True)
    articles = Article.objects.select_related('related_product')
    return render(request,
                  'shop/products/index.html',
                  {'products': products,
                   'articles': articles})

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request,
                  'shop/products/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    category = Category.objects.all()
    product = get_object_or_404(
        Product,
        id=id,
        slug=slug,
        available=True)

    return render(request,
                  'shop/products/detail.html',
                  {'product': product,
                   'category': category})


def article_detail(request, slug):
    products = Article.objects.select_related('related_product')
    # articles = get_object_or_404(
    #     Article,
    #     slug=slug)
    articles = Article.objects.all(slug=slug)
    return render(request,
                  'shop/articles/article_detail.html',
                  {'products': products,
                   'articles': articles})