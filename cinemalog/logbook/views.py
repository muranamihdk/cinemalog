from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Movie
from .forms import MovieCreateForm, MovieCreateWithITunesDataForm, MovieUpdateForm

import os
from urllib.parse import urlparse
import requests
from itunesstore.iTunesStoreAPI import iTunesStoreAPI



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

    def _create_image_file_name(self, image_url):
        img_path = urlparse(image_url)[2]
        file_name = '{}.{}'.format(img_path.split('/')[-3], img_path.split('/')[-1])
        return file_name

    def _create_image_path(self, image_file_name):
        local_path = os.path.join(os.path.dirname(__file__), 'static', 'logbook', 'images', image_file_name[:1], image_file_name)
        return local_path

    def _save_image(self, image_url, image_file_name):
        local_path = self._create_image_path(image_file_name)
        #r = requests.get(image_url)
        r = requests.get(image_url, stream=True)
        if r.status_code == 200:
            with open(local_path, 'wb') as f:
                #f.write(r.content)
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk: # filter out keep-alive new chunks
                        f.write(chunk)

    def get_initial(self):
        itunes = iTunesStoreAPI()
        results = itunes.lookup(self.kwargs['track_id'])
        movie = results['results'][0]
        img_url30 = self._create_image_file_name(movie['artworkUrl30'])
        img_url60 = self._create_image_file_name(movie['artworkUrl60'])
        img_url100 = self._create_image_file_name(movie['artworkUrl100'])
        self._save_image(movie['artworkUrl30'], img_url30)
        self._save_image(movie['artworkUrl60'], img_url60)
        self._save_image(movie['artworkUrl100'], img_url100)
        runtime = movie.get('trackTimeMillis', '')
        if runtime:
            if str(runtime).isdigit():
                minutes = int(runtime)//60000
                runtime = '{:d}時間{:d}分'.format(minutes//60, minutes%60)
        else:
            runtime = ''
        return {
            'track_id': movie['trackId'],
            'itunes_url': movie['trackViewUrl'],
            'preview_url': movie.get('previewUrl', ''),
            'img_url30': img_url30,
            'img_url60': img_url60,
            'img_url100': img_url100,
            'title': movie['trackName'],
            'director': movie['artistName'],
            'genre': movie['primaryGenreName'],
            'release': movie['releaseDate'][:4],
            'runtime': runtime,
        }
        #fields = ['date', 'track_id', 'itunes_url', 'preview_url', 'img_url30', 'img_url60', 'img_url100', 'title', 'director', 'genre', 'release', 'runtime', 'score', 'review']

        def form_valid(self, form):
            self.object = form.save()
            # do something with self.object
            return HttpResponseRedirect(self.get_success_url())


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
