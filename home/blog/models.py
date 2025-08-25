from django.db import models

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=50)
    slug = models.CharField(max_length=50, unique=True)
    timestamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + ' from ' + self.author
