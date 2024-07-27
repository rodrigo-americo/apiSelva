from django.db import models
from django.utils import timezone
# Create your models here.


class Usuario(models.Model):
    userName = models.CharField(max_length=150)
    password = models.CharField(max_length=30)
    active = models.BooleanField()
    datecreatedAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.userName
