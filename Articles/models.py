from django.db import models
from django.utils import timezone

class Articles(models.Model):
    title = models.CharField(max_length=200)
    subtitle=models.CharField(max_length=100,null=True,blank=True)
    content = models.TextField(blank=True)
    published_date = models.DateField(default=timezone.now)

    
    def __str__(self):
        return self.title
