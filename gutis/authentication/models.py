from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image = models.ImageField(upload_to="media/images/users", null=True, blank=True)
    remember_me = models.BooleanField(default=False)
    consent_to_data_processing = models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True)
    middle_name = models.CharField(max_length=150, blank=True, null=True)


# class User(models.Model):
#     surname
#     name
#     middle_name
#     date_of_birth
#     mail
#     password
#     remember_me
#     consent_to_data_processing
