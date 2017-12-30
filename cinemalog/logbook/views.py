from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Movie
from .forms import MovieCreateForm, MovieCreateWithITunesDataForm, MovieUpdateForm


class IndexView(generic.ListView):
    model = Movie
    paginate_by = 100
    template_name = 'movies/index.html'

    #queryset = Movie.objects.order_by('-date')
    def get_queryset(self):
        return Movie.objects.order_by('-date', '-id')


class DetailView(generic.DetailView):
    model = Movie
    template_name = 'movies/detail.html'


class MovieCreate(CreateView):
    model = Movie
    form_class = MovieCreateForm
    template_name = 'movies/create.html'
    #success_url = reverse_lazy('logbook:detail')


class MovieCreateWithITunesData(CreateView):
    model = Movie
    form_class = MovieCreateWithITunesDataForm
    template_name = 'movies/create_with_itunes_data.html'

    def get_initial(self):
        return {
            'track_id': self.kwargs['track_id'],
            #'itunes_url': self.kwargs[''],
            #'preview_url': self.kwargs[''],
            #'img_url30': self.kwargs[''],
            #'img_url60': self.kwargs[''],
            #'img_url100': self.kwargs[''],
            #'title': self.kwargs['title'],
            #'director': self.kwargs[''],
            #'genre': self.kwargs[''],
            #'release': self.kwargs[''],
            #'runtime': self.kwargs[''],
        }
        #fields = ['date', 'track_id', 'itunes_url', 'preview_url', 'img_url30', 'img_url60', 'img_url100', 'title', 'director', 'genre', 'release', 'runtime', 'score', 'review']

class MovieUpdate(UpdateView):
    model = Movie
    form_class = MovieUpdateForm
    template_name = 'movies/edit.html'


def delete(request, movie_id):
    #DeleteView Classで実装するとき
    #model = Author
    #success_url = reverse_lazy('logbook:index')
    movie = get_object_or_404(Movie, pk=movie_id)
    movie.delete()
    #return HttpResponseRedirect(reverse('logbook:index'))
    return redirect(reverse('logbook:index'))


class TopRedirect(generic.RedirectView):
    url = reverse_lazy('logbook:index')
