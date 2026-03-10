from django.contrib import admin
from django.urls import path, include   # добавили include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),     # подключили core
    # Встроенные маршруты аутентификации (вход/выход)
    path('accounts/', include('django.contrib.auth.urls')),
]