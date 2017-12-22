from django.db import models

CREATE TABLE cinemalog (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT NOT NULL, track_id TEXT, itunes_url TEXT, preview_url TEXT, img_url30 TEXT, img_url60 TEXT, img_url100 TEXT, title TEXT NOT NULL, director TEXT, genre TEXT, release TEXT, runtime TEXT, score INTEGER, review TEXT);
class Movie(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return "<{0}>".format(self.title)

class Book(models.Model):
    """書籍"""
    name = models.CharField('書籍名', max_length=255)
    publisher = models.CharField('出版社', max_length=255, blank=True)
    page = models.IntegerField('ページ数', blank=True, default=0)

    def __str__(self):
        return self.name


class Impression(models.Model):
    """感想"""
    book = models.ForeignKey(Book, verbose_name='書籍', related_name='impressions')
    comment = models.TextField('コメント', blank=True)

    def __str__(self):
        return self.comment
