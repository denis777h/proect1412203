from tempfile import template

from django.db import models
import re

from django.template import Library


# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=255, unique=0)
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Arc:
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

    pass


class Arctik:
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text
    pass



def censor(value):
    unwanted_words = ['нежелательное_слово1', 'нежелательное_слово2']  #

    for word in unwanted_words:
        value = re.sub(r'\b{}\b'.format(word), '*' * len(word), value, flags=re.IGNORECASE)

    return value