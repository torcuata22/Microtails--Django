from django.db import models

# Create your models here.
class Tales(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=150)
    genre = models.CharField(max_length=150)
    date_created = models.DateField(null=False)
    content = models.TextField(blank=False, null=False)
    featured_tale=models.BooleanField() #null=True, or set default=True

