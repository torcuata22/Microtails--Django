from django.db import models

# Create your models here.
class Tales(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=150)
    genre = models.CharField(max_length=150)
    content = models.TextField(blank=False, null=False)
    featured_tale=models.BooleanField(default=True) #null=True, or set default=True

