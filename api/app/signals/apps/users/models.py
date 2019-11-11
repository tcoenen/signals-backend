from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext as _

from signals.apps.signals.models.mixins import CreatedUpdatedModel


class Profile(CreatedUpdatedModel):
    """
    The profile model for a user
    """

    user = models.OneToOneField(
        to=User,
        related_name='profile',
        verbose_name=_('profile'),
        on_delete=models.DO_NOTHING,
    )

    departments = models.ManyToManyField(
        to='signals.Department',
    )

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'profile'):
        Profile.objects.create(user=instance)