from django.db import models

class Document(models.Model):
    name = models.CharField(max_length=200)
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class DocPage(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    text = models.TextField(blank=True)
    files = models.ManyToManyField(Document)