from django.db import models
from django.core.urlresolvers import reverse


class Post(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(
        max_length = 200,
        blank = True)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural = 'Posts'
    
    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={
            'post_id':self.id})
