from django.db import models

# Create your models here.

class Blog(models.Model):
    def upload_blog_image(instance,filename):
        import os
        return os.path.join(f"blog_image/{instance}",filename)
    image = models.ImageField(upload_to=upload_blog_image)
    title = models.CharField(max_length=255)
    description = models.TextField()