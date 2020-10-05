from datetime import datetime

from django.db import models


class Category(models.Model):
    '''Категория товара'''

    name = models.CharField(
        max_length=40,
        db_index=True
    )

    slug = models.SlugField(
        max_length=40,
        unique=True
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = "Категорий"

    def __str__(self):
        return self.name


class Product(models.Model):
    '''Товар'''

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='media/products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товаров'

    def __str__(self):
        return self.name


class Article(models.Model):
    '''Статья на главную'''

    header = models.CharField(max_length=100, null=False, blank=False, default='')
    text = models.TextField(max_length=2500, null=True, blank=True)
    image = models.ImageField(upload_to='media/articles/%Y/%m/%d', blank=True)
    related_product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статей'

    def __str__(self):
        return f'{self.header}'