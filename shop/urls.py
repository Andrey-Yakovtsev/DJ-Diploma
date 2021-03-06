from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    # path('<slug:slug>/', views.product_detail, name='product_detail'),
    path('', views.main_page, name='main_page'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('<slug:category_slug>/<slug:article_slug>/', views.article_detail, name='article_detail'),
]