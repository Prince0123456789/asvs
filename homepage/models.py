from django.db import models

# Create your models here.
class HomepageCarouselImage(models.Model):
    def upload_image_path(instance,filename):
        import os 
        return os.path.join(f"hmoepagecarousel/",filename)
    images = models.ImageField(upload_to=upload_image_path)

