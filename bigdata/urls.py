from django.contrib import admin
from django.urls import path
from Empresas.views import lista_empresas,detalle_empresa, home
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lista_empresas, name='lista_empresas'),
    path('empresa/<int:empresa_id>/', detalle_empresa, name='detalle_empresa'),
    
]# Servir archivos multimedia en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
