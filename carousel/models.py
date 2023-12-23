from django.db import models

# Create your models here.

class CarouselImage(models.Model):
    def image_upload_to(instance,filename):
        import os
        return os.path.join(f"carousel_img/{instance.id}",filename)
    image = models.ImageField(upload_to=image_upload_to)