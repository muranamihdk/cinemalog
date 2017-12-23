from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Movie

# Create your views here.
def index(request):
    latest_movie_list = Movie.objects.order_by('-date')[:5]
    output = ', '.join([q.title for q in latest_movie_list])
    return HttpResponse(output)

def detail(request, movie_id):
    return HttpResponse("You're looking at movie %s." % movie_id)

def results(request, movie_id):
    response = "You're looking at the results of movie %s."
    return HttpResponse(response % movie_id)

def vote(request, movie_id):
    return HttpResponse("You're voting on movie %s." % movie_id)