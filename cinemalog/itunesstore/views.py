from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.http import HttpResponse
from .forms import SearchForm
from . iTunesStoreAPI import search_movie



def index(request):
    return render(request, 'itunesstore/index.html')


def results(request):
    results = search_movie(request.GET.get('search_key'))
    d = {
        'movie_list': results
    }
    return render(request, 'itunesstore/results.html', d)


def detail(request, trackid):
    return HttpResponse("You're looking at question %s." % trackid)
