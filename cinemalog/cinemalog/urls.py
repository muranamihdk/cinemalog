"""cinemalog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.contrib import admin
from logbook.views import TopRedirect

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', TopRedirect.as_view(), name='redirect-to-list'),
    path(r'movies/', include('logbook.urls'), name='logbook'),
    path(r'itunesstore/', include('itunesstore.urls'), name='itunesstore'),
]
