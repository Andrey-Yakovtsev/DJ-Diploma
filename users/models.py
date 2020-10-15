from django.db import models
from django.contrib.auth.models import User
from orders.models import Order


class SiteUser(User):
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    orders = models.ManyToManyField(Order, related_name='users', through='UsersOrders')

    class Meta:
        ordering = ('last_name',)
        verbose_name = 'Покупатель'
        verbose_name_plural = "Покупатели"

    # def __str__(self):
    #     return f'{self.username} - {self.first_name} - {self.last_name}'



class UsersOrders(models.Model):
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
