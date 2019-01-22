from django.db import models
from django.conf import settings
from django.db.models import Q

# Create your models here.
# blog.models



class PostManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(title__icontains=query) |
                         Q(description__icontains=query)

                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)

    publish_date = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = PostManager()


# courses.models
class Lesson(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)

    featured = models.BooleanField(default=False)
    publish_date = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
    objects = PostManager()

# profiles.models
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)

    timestamp = models.DateTimeField(auto_now_add=True)
    objects = PostManager()