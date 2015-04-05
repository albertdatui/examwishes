from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from django.dispatch import receiver

@receiver(post_save, sender=User)
def callback_user_created(sender, instance=None, created=False, **kwargs):
    if created:
        user = instance
        admin_group, created = Group.objects.get_or_create(name='Admin')
        manager_group, created = Group.objects.get_or_create(name='Manager')
        customer_group, created = Group.objects.get_or_create(name='Customer')
        customer_group.user_set.add(user)
