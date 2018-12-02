from django.db import models

# table
class Post(models.Model):
    #coloum
    title = models.CharField(max_length = 140)
    body = models.TextField()
    date = models.DateTimeField()

    #meta reference
    def __str__(self):
        return self.title

    
