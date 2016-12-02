# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from _json import make_encoder


from django.db import models
from django.contrib.postgres.fields.jsonb import JSONField
from django.contrib.postgres.fields import ArrayField

import os

# Create your models here.

class Actions(models.Model):
    name = models.CharField('Заголовок', max_length=150)
    foto = ArrayField(models.CharField(max_length=1000), verbose_name='Фото', default=[])
    actual = models.BooleanField('Актуальность', default=True)

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

    def __str__(self):
        return self.name