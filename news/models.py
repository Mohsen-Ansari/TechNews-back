from django.db import models


# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class Reference(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    date = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    references = models.ManyToManyField(Reference)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'News'
