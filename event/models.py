from django.db import models

class Event(models.Model):
    def upload_event_image(instance,filename):
        import os
        return os.path.join(f"event/{instance.name}",filename)
    image = models.ImageField(upload_to=upload_event_image)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    event_date_time =  models.DateTimeField()
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name