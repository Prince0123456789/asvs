from django.db import models


class Health(models.Model):
    text = models.TextField()

    def __str__(self) -> str:
        return self.text

class Environment(models.Model):
    text = models.TextField()

    def __str__(self) -> str:
        return self.text

class Education(models.Model):
    text = models.TextField()

    def __str__(self) -> str:
        return self.text
    
class SocialCare(models.Model):
    text = models.TextField()

    def __str__(self) -> str:
        return self.text
