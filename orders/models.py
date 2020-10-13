from django.db import models
from shop.models import Product


class Order(models.Model):
    username = models.CharField(max_length=40, verbose_name='Ваш логин для сайта')
    first_name = models.CharField(max_length=40, verbose_name='Имя')
    last_name = models.CharField(max_length=40, verbose_name='Фамилия')
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=250, verbose_name='Адрес')
    city = models.CharField(max_length=20, verbose_name='Город')
    phone = models.CharField(max_length=11, verbose_name='Номер телефона')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
