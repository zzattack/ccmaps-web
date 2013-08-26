from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from ccmaps.maps.models import GAMES    

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)
    favorite_game = models.CharField(max_length=50, choices=GAMES, blank=False)
    website = models.URLField(verify_exists = False, default='', blank=True)
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female'), (' ', 'Not specified')), default='M', blank=True)
    location = models.CharField(max_length=100, default='', blank=True)
    bio = models.TextField(default='', blank=True)
    def get_absolute_url(self):
        return ('profiles_profile_detail', (), { 'username': self.user.username })
    get_absolute_url = models.permalink(get_absolute_url)
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)