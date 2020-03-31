from django.db import models

# Create your models here.
class Post(models.Model):
    sl_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=75)
    content = models.TextField()
    author = models.CharField(max_length=30)
    timeStamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + ' by ' + self.author