from django.contrib.auth import get_user_model 
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import UserDetails, OTP
from django.conf import settings
# from authentication.models import UserDetails

@receiver(post_save, sender=UserDetails)
def generate_otp(sender, instance, created, **kwargs):
    if created:
        print('created NEW USER')
    else:    
        print('not created')
        
    if instance.phone:
        if not instance.user.is_phone_validated:
            OTP.objects.create(user=instance.user, pin='1234')
post_save.connect(generate_otp,sender=UserDetails)
