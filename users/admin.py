from django.contrib import admin
from.models import SiteUser

@admin.register(SiteUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name',
                    'phone', 'email', 'address', 'city',
                    ]

