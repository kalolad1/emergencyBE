from django.db import models


class Link(models.Model):
    name = models.CharField(max_length=100, blank=True)
    link = models.URLField()

    def __str__(self):
        return self.name

