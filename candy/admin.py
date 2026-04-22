from django.contrib import admin
from .models import Category, Candies


# Register your models here.

admin.site.empty_value_display = 'Не задано'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_published',
    )

    list_editable = ('is_published',)


@admin.register(Candies)
class CandiesAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_published',
        'is_on_main',
        'description',
        'category',
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category',
    )

    empty_value_display = 'Не задано'
    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)
