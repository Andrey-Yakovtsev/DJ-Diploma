from django import forms

from users.models import SiteUser
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'city', 'address']

    def clean_username(self):
        username = self.cleaned_data['username']
        return username.strip()

    def clean(self):
        username = self.cleaned_data['username']
        existing_user_query = SiteUser.objects.filter(
            username=username
        )
        if existing_user_query.exists():
            forms.ValidationError('Пользователь с таким ником уже существует. Войдите в систему')
        return self.cleaned_data