#blog/urls.py
from django.urls import path
from .views import VistaListaBlog
from .views import VistaDetalleBlog, VistaCrearEntradaBlog, VistaEditarEntradaBlog,VistaEliminarEntradaBlog


urlpatterns = [
path('',VistaListaBlog.as_view(), name=('inicio')),
path('pub/<int:pk>/',VistaDetalleBlog.as_view(), name='detalle_pub'),
path('pub/nueva/', VistaCrearEntradaBlog.as_view(), name = 'pub_nuevo'),
path('pub/<int:pk>/editar', VistaEditarEntradaBlog.as_view(), name='editar_pub'), 
path('pub/<int:pk>/eliminar/', VistaEliminarEntradaBlog.as_view(), name='eliminar_pub'),
#aqui talvez sea .html
]