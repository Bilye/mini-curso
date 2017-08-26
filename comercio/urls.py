from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.PaginaPrimera.as_view(), name="pagina-primera" ),
    url(r'^productos/$', views.PaginaProductos.as_view(), name="pagina-productos" ),
]
