from django.conf.urls import url,include
from .views import RegistroCaras,  crearUsuario


urlpatterns = [
   url(r'^caras/', RegistroCaras, name='caras'),
url(r'^registrar/', crearUsuario, name='registrar_usuario'),
    
]