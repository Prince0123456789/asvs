from django.db import models

# Create your models here.
class NgoLogo(models.Model):
    title = models.CharField(max_length=255,default="",null=True,blank=True)
    def get_upload_path(instance,filename):
        import os
        return os.path.join(f"ngo_logo/{instance.title}",filename)

    logo = models.ImageField(upload_to=get_upload_path)


class Carousel(models.Model):
    title = models.CharField(max_length=255,null=True,blank=True)
    def get_upload_path(instance,filename):
        import os
        return os.path.join(f"carousel/{instance.title}",filename)
    image = models.ImageField(upload_to=get_upload_path)
    priority = models.IntegerField()

    def __str__(self) -> str:
        return self.title
    
class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self) -> str:
        return f"{self.name} -- > {self.subject}"