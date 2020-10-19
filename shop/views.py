from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Article, Review
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator
from urllib.parse import urlencode
from .forms import ReviewForm
from django.urls import reverse


def main_page(request):
    category = Category.objects.filter(parent_category=None)
    # subcategories = Category.objects.filter(parent_category__isnull=False)
    products = Product.objects.filter(available=True)
    articles = Article.objects.all()
    cart_product_form = CartAddProductForm()
    paginator = Paginator(list(products), 4)
    current_page = request.GET.get('page', 1)
    page_obj = paginator.get_page(current_page)
    return render(request,
                  'shop/products/index.html',
                  {'articles': articles,
                   'category': category,
                   # 'subcategories': subcategories,
                   'cart_product_form': cart_product_form,
                   'products': page_obj,
                   'current_page': current_page,
                   'prev_page_url': '?' + urlencode({
                       'page': page_obj.previous_page_number()}) if page_obj.has_previous() else None,
                   'next_page_url': '?' + urlencode({
                       'page': page_obj.next_page_number()}) if page_obj.has_next() else None
                   })

def product_list(request, category_slug=None):
    # category = None
    category = Category.objects.filter(parent_category=None)
    subcategories = Category.objects.filter(parent_category__isnull=False)
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        if not products:
            products = Product.objects.select_related('category').filter(category__parent_category=int(category.id))

    cart_product_form = CartAddProductForm()
    paginator = Paginator(list(products), 4)
    current_page = request.GET.get('page', 1)
    page_obj = paginator.get_page(current_page)

    return render(request,
                  'shop/products/list.html',
                  {'category': category,
                   'subcategories': subcategories,
                   'cart_product_form': cart_product_form,
                    'products': page_obj,
                    'current_page': current_page,
                    'prev_page_url': '?' + urlencode({
                        'page': page_obj.previous_page_number()}) if page_obj.has_previous() else None,
                    'next_page_url': '?' + urlencode({
                        'page': page_obj.next_page_number()}) if page_obj.has_next() else None
                   })

def product_detail(request, id, slug):
    category = Category.objects.filter(parent_category=None)
    subcategories = Category.objects.filter(parent_category__isnull=False)
    reviews = Review.objects.select_related('product').all()
    product = get_object_or_404(
        Product,
        id=id,
        slug=slug,
        available=True)
    cart_product_form = CartAddProductForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            Review.objects.create(text=form.cleaned_data['text'], product_id=product.id)

            return redirect('shop:product_detail') #, product.id)
    else:
        form = ReviewForm()

    return render(request,
                  'shop/products/detail.html',
                  {'product': product,
                   'category': category,
                   'reviews': reviews.filter(product_id=product.id),
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