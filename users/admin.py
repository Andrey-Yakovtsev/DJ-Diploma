from django.contrib import admin
from.models import SiteUser, UsersOrders


class UsersOrdersInline(admin.TabularInline):
    model = UsersOrders
    extra = 1


@admin.register(SiteUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name',
                    'phone', 'email', 'address', 'city',
                    ]
    inlines = [UsersOrdersInline]
