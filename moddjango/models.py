from django.db import models


class Module(models.Model):
    name = models.CharField(max_length = 255, unique = True)
    description = models.TextField()
    version = models.CharField(max_length = 50)
    status = models.CharField(max_length = 10, default='downloaded')
    migrate = models.BooleanField(default=False)
    templates = models.BooleanField(default=False)
    urls = models.BooleanField(default=False)
    dependence = models.ManyToManyField(
        "self",
        symmetrical=False,
        blank=True,
        null=True)

info_posts = {
    "name":"posts",
    "description":"just added posts list and details for post. with this module u can add ur post in django-admin-panel and look it in ur website",
    "version":"0.1",
    "dependencies":[],
    "migrate":"True",
    "templates":"True",
    "urls":"True"
}

info_comments = {
    "name":"comments",
    "description":"added comments for posts. with this module anyone can add comment for ur posts",
    "version":"0.1.2",
    "dependencies":["posts"],
    "migrate":"True",
    "templates":"True",
    "urls":"True"
}
