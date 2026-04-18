from django.db import models
from core.models import PublishedModel

# Create your models here.
class Category(PublishedModel, models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    slug = models.SlugField(max_length=64, unique=True, verbose_name='Слаг')
    output_order = models.PositiveSmallIntegerField(default=100, verbose_name='Порядок отображения')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Candies(PublishedModel, models.Model):
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    is_on_main = models.BooleanField(default=True, verbose_name='На главной')
    title = models.CharField(max_length=128, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'Сладость'
        verbose_name_plural = 'Сладости'

    def __str__(self):
        return self.title
