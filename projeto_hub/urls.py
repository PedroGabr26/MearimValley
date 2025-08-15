"""projeto_hub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    #ROTAS API
    path('api/', include('parceiros.urls_api')), # adiciona as rotas do backend do app parceiros ao meu projeto.
    path('api/', include('noticias.urls_api')),
    path('api/', include('editais.urls_api')),
    path('api/', include('cursos.urls_api')),
    #ROTAS FRONT
    path('parceiros/', include('parceiros.urls')), # adiciona as rotas do frontend do app parceiros
    path('noticias/', include('noticias.urls')),
    path('edital/', include('editais.urls')),
    path('cursos/', include('cursos.urls')),
    path('home/',home, name='home'),
    path('sobre/',sobre, name='sobre'),
    path('contatos/',contatos, name='contatos'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)