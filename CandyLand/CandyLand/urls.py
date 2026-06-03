from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('candy/', include('candy.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    # path('', include('users.urls'))
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Куда перенаправлять пользователя ПОСЛЕ успешного входа
LOGIN_REDIRECT_URL = '/users/my-profile/'

# Куда перенаправлять пользователя, если он не авторизован, но пытается зайти в профиль
LOGIN_URL = '/accounts/login/'

# Куда перенаправлять пользователя ПОСЛЕ выхода из аккаунта
LOGOUT_REDIRECT_URL = '/accounts/login/'

