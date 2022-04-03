from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_organisor = models.BooleanField(default=True, blank=True, null=True)
    is_agent = models.BooleanField(default=False, blank=True, null=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.user.username


class CustomUser(models.Model):
    agent = models.ForeignKey('Agent', on_delete=models.SET_NULL, blank=True, null=True)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.user.email


def post_user_crated_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_crated_signal, sender=User)