# models.py
# from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
        )
    name_user = models.CharField(max_length=20, verbose_name='Никнейм', default='ueser')
    email_user = models.TextField(verbose_name='Маил почта', blank=True)
    avatar = models.ImageField(upload_to='img/profile.png')

    class Meta():
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.user.username
