from django.http.response import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import Movie

# Create your views here.
def index(request):
    latest_movie_list = Movie.objects.order_by('-date')[:5]
    context = {'latest_movie_list': latest_movie_list,}
    return render(request, 'movies/index.html', context)

def detail(request, movie_id):
	movie = get_object_or_404(Movie, pk=movie_id)
	return render(request, 'movies/detail.html', {'movie': movie})

def results(request, movie_id):
    response = "You're looking at the results of movie %s."
    return HttpResponse(response % movie_id)

def vote(request, movie_id):
    return HttpResponse("You're voting on movie %s." % movie_id)