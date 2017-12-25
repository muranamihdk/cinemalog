from datetime import date
from django.urls import reverse
from django.db import models

class Movie(models.Model):
    """映画"""
    #id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL
    date = models.DateField("視聴日", default=date.today)
    track_id = models.CharField("トラックID", max_length=20, blank=True)
    itunes_url = models.URLField("iTunesStore URL", blank=True)
    preview_url = models.URLField("プレビューURL", blank=True)
    img_url30 = models.URLField("Height30画像URL", blank=True)
    img_url60 = models.URLField("Height60画像URL", blank=True)
    img_url100 = models.URLField("Height100画像URL", blank=True)
    title = models.CharField("タイトル", max_length=50)
    director = models.CharField("監督", max_length=20, blank=True)
    genre = models.CharField("ジャンル", max_length=10, blank=True)
    release = models.CharField("リリース", max_length=4, blank=True)
    runtime = models.CharField("上映時間", max_length=10, blank=True)
    score = models.IntegerField("スコア", default=3, choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    review = models.TextField("レビュー", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
            return reverse('logbook:detail', kwargs={'pk': self.pk})    
