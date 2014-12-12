from django.db import models


class Module(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.TextField()
    version = models.CharField(max_length = 50)
