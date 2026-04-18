from django.urls import path

from . import views

app_name = 'candy'

urlpatterns = [
    path('', views.candy_list, name='candy_list'),
    path('<int:pk>/', views.candy_detail, name='candy_detail')
]
