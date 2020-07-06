from django.db import models
from django.contrib.auth.models import User
from events.models import Event


# Create your models here.
class CustomUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)



