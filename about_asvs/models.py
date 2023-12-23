from django.db import models

class AboutNgo(models.Model):
    about = models.TextField()

    def __str__(self):
        return self.about
    

class Mission(models.Model):

    mission = models.TextField()

    def __str__(self) -> str:
        return self.mission
    

class Vision(models.Model):
    vision = models.TextField()

    def __str__(self) -> str:
        return self.vision
