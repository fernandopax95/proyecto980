
from django.conf.urls import url,include
from .views import index, mascota_delete, mascota_view, mascota_list, mascota_edit, mascota_list_images


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo/', mascota_view, name = "mascota_crear"),
    url(r'^listar/', mascota_list, name = "mascota_listar"),
    url(r'^listarimagen/', mascota_list_images, name = "mascota_listar_imagenes"),
    url(r'^editar/(?P<folio_mascota>\d+)/', mascota_edit, name = "mascota_editar"),
    url(r'^eliminar/(?P<folio_mascota>\d+)/', mascota_delete, name = "mascota_eliminar"),
]
