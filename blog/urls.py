#blog/urls.py
from django.urls import path
from .views import VistaListaBlog
from .views import VistaDetalleBlog

urlpatterns = [
path('',VistaListaBlog.as_view(), name=('inicio')),
path('pub/<int:pk>/',VistaDetalleBlog.as_view(), name='detalle_pub') #aqui talvez sea .html
]