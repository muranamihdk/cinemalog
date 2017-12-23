from django.urls import path
from . import views

# Create your views here.
urlpatterns = [
    # ex: /movies/
    path('', views.index, name='index'),
    # ex: /movies/5/
    path('<int:movie_id>/', views.detail, name='detail'),
    # ex: /movies/5/results/
    path('<int:movie_id>/results/', views.results, name='results'),
    # ex: /movies/5/vote/
    path('<int:movie_id>/vote/', views.vote, name='vote'),
]
