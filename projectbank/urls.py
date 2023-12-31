"""projectbank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path, include
from rest_framework.documentation import include_docs_urls
from django.conf import settings
from django.conf.urls.static import static

#urls errores 
from django.conf.urls import handler404 , handler500 
from applications.home.views import Error404 , Error500 , Error503

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='Banco de Proyectos API')),
    re_path('', include('applications.projects.urls')),
    re_path('', include('applications.home.urls')),
    re_path('', include('applications.users.urls')),
    re_path('', include('applications.regioncomuna.urls')),
    
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = Error404.as_view()

handler500 = Error500.as_error_view()

urlpatterns += [
path('503/', Error503.as_error_view(), name='error_503'), 

]