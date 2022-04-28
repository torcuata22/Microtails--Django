from django.db import models
from django.urls import reverse

# Create your models here.
class Tales(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=150)
    genre = models.CharField(max_length=150)
    content = models.TextField(blank=False, null=False)
    featured_tale=models.BooleanField(default=True) #null=True, or set default=True

    def get_absolute_url (self):
        return reverse("tales:list-of-tales", kwargs={"id": self.id}) #f"/tales/{self.id}/"

