# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Blog(models.Model):
    class Meta:
        db_table = 'weblog_blogs'

    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name
