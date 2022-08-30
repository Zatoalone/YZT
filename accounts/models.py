from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from core.models import Company


class JobTitle(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название должности")
    description = models.TextField(blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.OneToOneField(Company, on_delete=models.CASCADE)
    title = models.OneToOneField(JobTitle, on_delete=models.CASCADE)

    def __str__(self):
        return self




@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


