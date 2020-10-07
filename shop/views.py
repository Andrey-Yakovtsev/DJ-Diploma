from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Article
from cart.forms import CartAddProductForm

def main_page(request):
    products = Product.objects.filter(available=True)
    articles = Article.objects.all()
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/products/index.html',
                  {'products': products,
                   'articles': articles,
                   'cart_product_form': cart_product_form})

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    cart_product_form = CartAddProductForm()

    return render(request,
                  'shop/products/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'cart_product_form': cart_product_form})


def product_detail(request, id, slug):
    category = Category.objects.all()
    product = get_object_or_404(
        Product,
        id=id,
        slug=slug,
        available=True)
    cart_product_form = CartAddProductForm()

    return render(request,
                  'shop/products/detail.html',
                  {'product': product,
                   'category': category,
                   'cart_product_form': cart_product_form})



def article_detail(request, category_slug, article_slug):
    products = Product.objects.select_related('category')
    cart_product_form = CartAddProductForm()
    article = get_object_or_404(Article, slug=article_slug)
    return render(request,
                  'shop/articles/article_detail.html',
                  {'products': products,
                    'article': article,
                    'cart_product_form': cart_product_form
                   })