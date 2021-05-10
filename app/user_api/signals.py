from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User
from .views import sio


@receiver(post_save, sender=User)
def send_update_push(sender, instance, created, **kwargs):
    """Send message when user updated."""
    if not created:
        sio.emit('message', {'user': f'{instance.first_name}/{instance.email}'})
