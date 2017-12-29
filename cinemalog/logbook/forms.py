from django.forms import ModelForm, RadioSelect
from .models import Movie

# Create the form class.
class MovieCreateForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['date', 'title', 'director', 'release', 'runtime', 'score', 'review']

class MovieUpdateForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['date', 'track_id', 'itunes_url', 'preview_url', 'img_url30', 'img_url60', 'img_url100', 'title', 'director', 'genre', 'release', 'runtime', 'score', 'review']
