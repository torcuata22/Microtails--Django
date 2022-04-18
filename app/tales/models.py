from django.db import models

# Create your models here.
class Tales():
    title = models.TextField(50)
    author = models.TextField (100)
    genre = models.TextField(50)
    date_created = models.DateTimeField()
    content = models.TextField(2000)

