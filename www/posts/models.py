from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    """ Post docstring """
    user = models.ForeignKey(User, related_name='posts')
    title = models.CharField(max_length=128)
    slug = models.SlugField(blank=True)
    content = models.TextField(default='', blank=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta(object):
        """ Meta """
        ordering = ['-posted_on', 'title']

    def __str__(self):
        return self.title
