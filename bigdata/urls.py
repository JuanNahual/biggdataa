from django.contrib import admin
from django.urls import path
from Empresas.views import lista_empresas,detalle_empresa, home
from django.conf.urls.static import static
from django.conf import settings
# import serve and repath
from django.views.static import serve
from django.urls import path, include,re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lista_empresas, name='lista_empresas'),
    path('empresa/<int:empresa_id>/', detalle_empresa, name='detalle_empresa'),
re_path(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    
]# Servir archivos multimedia en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
