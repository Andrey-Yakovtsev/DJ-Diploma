from django.db import models
from django.contrib.auth.models import AbstractUser
from orders.models import Order


class User(models.Model):
    user_name = models.CharField(max_length=40)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    class Meta:
        ordering = ('last_name',)
        verbose_name = 'Покупатель'
        verbose_name_plural = "Покупатели"

    def set_password(self, raw_password): #Эта функция работает криво. Надо либо переунаследоваться от АбстрактЮзер
                                    #либо разобраться как правильно этот хэш в базу писать...
        return raw_password
