from django.db import models

# Create your models here.
class Tales(models.Model):
    title = models.TextField()
    author = models.TextField ()
    genre = models.TextField()
    date_created = models.DateTimeField()
    content = models.TextField()

