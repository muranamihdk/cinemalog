from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView 

from .models import Movie
from .forms import MovieForm


# Create your views here.
class IndexView(generic.ListView):
    model = Movie
    paginate_by = 20
    template_name = 'movies/index.html'

    #queryset = Movie.objects.order_by('-date')
    def get_queryset(self):
        return Movie.objects.order_by('-date', '-id')


class DetailView(generic.DetailView):
    model = Movie
    template_name = 'movies/detail.html'


class MovieCreate(CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movies/add.html'
    #success_url = reverse_lazy('logbook:detail')


class MovieUpdate(UpdateView):
    model = Movie
    fields = ['date', 'track_id', 'itunes_url', 'preview_url', 'img_url30', 'img_url60', 'img_url100', 'title', 'director', 'genre', 'release', 'runtime', 'score', 'review']
    template_name = 'movies/edit.html'


def delete(request, movie_id):
    #model = Author
    #success_url = reverse_lazy('logbook:index')
    movie = get_object_or_404(Movie, pk=movie_id)
    movie.delete()
    return HttpResponseRedirect(reverse('logbook:index'))
