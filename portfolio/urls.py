"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

# import serve and repath
from django.views.static import serve #kete
from django.urls import path, include,re_path# edhe kete 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("folio.urls")),
    path("projects/", include("projects.urls")),
    path('api/', include('api.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')), 
    re_path(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),# me kete path bera te mundur qe media files te shfaqet ne production edhe me ato 2 importet
] 


# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
