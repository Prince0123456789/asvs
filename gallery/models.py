from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.

def slugcreator(instance):
    slug = slugify(instance.title)
    if GalleryCategory.objects.filter(slug=slug).exists():
        slug = slugify(instance.title)+"_0"
    return slug

class GalleryCategory(models.Model):
    title = models.CharField(max_length=255,default="")
    description = models.TextField(default="",null=True,blank=True)
    slug = models.SlugField(default="",null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    def save(self):
        if not self.slug:
            self.slug = slugcreator(self)
        super(GalleryCategory,self).save()




class GalleyImages(models.Model):
    category = models.ForeignKey(GalleryCategory,on_delete=models.CASCADE,related_name="images")
    def get_upload_path(instance,filename):
        import os
        return os.path.join(f"gallry_images/{instance.category.title}",filename)
    image = models.ImageField(upload_to=get_upload_path)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.category)