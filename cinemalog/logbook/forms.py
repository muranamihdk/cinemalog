from django.forms import ModelForm, RadioSelect, Textarea
from .models import Movie


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['date', 'track_id', 'itunes_url', 'preview_url', 'img_url30', 'img_url60', 'img_url100', 'title', 'director', 'genre', 'release', 'runtime', 'score', 'review']
        widgets = {
            'score': RadioSelect,
            'review': Textarea(attrs={'cols': 46,}),
        }
