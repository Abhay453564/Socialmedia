from django.db import models

# Create your models here.

class Post(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='posts',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description[:50]
    
class Reel(models.Model):
    caption = models.TextField()
    reel = models.FileField(upload_to='reels',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption[:50]
    
class Video(models.Model):
    title = models.TextField()
    v_description = models.TextField()
    video = models.FileField(upload_to='videos',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title[:50]