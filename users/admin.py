from django.contrib import admin
from .models import Profile

# Register your models here.

admin.site.empty_value_display = 'Не задано'


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'name_user',
        'email_user',
        'avatar',
        # 'avatar',
        # 'bio',
        # 'phone',
    )
    empty_value_display = 'Не задано'
    search_fields = ('user',)
