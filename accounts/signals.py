from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User, Group
from .models import Customer


# @receiver(post_save, sender=User)
def customer_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_superuser:
            group = Group.objects.get(name='admin')
            instance.groups.add(group)
        else:
            group = Group.objects.get(name='customer')
            instance.groups.add(group)


        Customer.objects.create(
            user=instance,
            name=instance.username,
            email=instance.email
        )
        print('Customer created!')

post_save.connect(customer_profile, sender=User)

# @receiver(post_save, sender=User)
# def update_profile(sender, instance, created, **kwargs):
#     if created == False:
#         instance.profile.save()
#         print('Customer updated!')

# post_save.connect(update_profile, sender=User)

        