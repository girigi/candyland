from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'profile'

urlpatterns = [
    path('my-profile/', views.profile_view, name='profile_view'),
    path('profile/<str:username>/', views.profile_view, name='profile_detail'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('delete-avatar/', views.delete_avatar, name='delete_avatar'),
    path('profile/update-field/', views.update_field, name='update_field'),
    path('logout/', LogoutView.as_view(), name='exit_profile'),
    path('register/', views.register, name='register'),
]

# Для разработки (не использовать в production)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
