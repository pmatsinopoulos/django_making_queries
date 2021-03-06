# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Author(models.Model):
    class Meta:
        db_table = 'weblog_authors'

    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name
