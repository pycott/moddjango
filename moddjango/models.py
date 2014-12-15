from django.db import models


class Module(models.Model):
    name = models.CharField(max_length = 255, unique = True)
    description = models.TextField()
    version = models.CharField(max_length = 50)
    status = models.CharField(max_length = 10)
    dependencies = models.ManyToManyField("self", symmetrical=False)
    migrate = models.BooleanField(default=False)
