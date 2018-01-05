from django.urls import path
from . import views

app_name = 'logbook'
urlpatterns = [
    # ex: /movies/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /movies/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /movies/5/edit/
    path('<int:pk>/edit/', views.MovieUpdate.as_view(), name='edit'),
    # ex: /movies/5/delete/
    path('<int:movie_id>/delete/', views.delete, name='delete'),
    # ex: /movies/add/?track_id=1234567
    path('add/?track_id=<int:track_id>', views.MovieCreateWithITunesData.as_view(), name='addwithdata'),
    # ex: /movies/add/
    path('add/', views.MovieCreate.as_view(), name='add'),
]
