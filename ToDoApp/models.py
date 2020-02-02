from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item + " | " + str(self.completed)
