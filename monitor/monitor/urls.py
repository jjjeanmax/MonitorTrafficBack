from django.contrib import admin
from django.urls import path, include

from monitor.yasg import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),#monitor app url
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
