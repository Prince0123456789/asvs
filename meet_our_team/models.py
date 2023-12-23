from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)

    def upload_team_image(instance,filename):
        import os
        return os.path.join(f"team_members/{instance.name}",filename)

    image = models.ImageField(upload_to=upload_team_image)
    is_active = models.BooleanField(default=True)
    facebook_link = models.CharField(default="",max_length=255,null=True,blank=True)
    twiiter_link = models.CharField(default="",max_length=255,null=True,blank=True)

    def __str__(self) -> str:
        return f"{self.name} -- > {self.position}"