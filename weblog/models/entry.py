from django.db import models

from .blog import Blog
from .author import Author


class Entry(models.Model):
    class Meta:
        db_table = 'weblog_entries'

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255, default=None)
    body_text = models.TextField(default=None)
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()

    def __str__(self):
        return self.headline

