from django.db import models

class Volunteer(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255)
    why_to_become_volunteer = models.TextField(null=True,blank=True)

    def __str__(self) -> str:
        return f"{self.email}-->{self.name}"