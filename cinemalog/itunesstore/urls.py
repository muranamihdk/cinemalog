from django.urls import path

from . import views

app_name = 'itunesstore'
urlpatterns = [
    # ex: /itunesstore/
    path('', views.index, name='index'),
    # ex: /itunesstore/results/
    path('results/', views.results, name='results'),
    # ex: /itunesstore/5/
    path('<int:trackid>/', views.detail, name='detail'),
]
