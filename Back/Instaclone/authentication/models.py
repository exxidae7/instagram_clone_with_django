from django.db import models
from django.utils import timezone
import django.utils
import datetime
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50 )
    userName = models.CharField(max_length=50)
    website = models.URLField(blank=True)
    bio = models.TextField(max_length=500)
    gender = models.BooleanField(default=False)
    email = models.EmailField(max_length=200)
    count_post =  models.IntegerField(default=0)
    follow = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)
    created = models.DateField(default=django.utils.timezone.now)
    pic = models.ImageField(upload_to= 'profile_pic' , blank=True , null=None , verbose_name="profile_pic")
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    namePost = models.ForeignKey(User , on_delete=models.CASCADE)
    postId = models.SlugField(max_length=255, db_index=True)
    image = models.ImageField(upload_to='upload/')
    dataPost = models.DateTimeField()
    caption = models.TextField(max_length=1000)
    like = models.IntegerField()
    comment = models.TextField(max_length=2000)
    
    def __str__(self):
        return self.namePost


def create_user_profile(sender , instance, created , **kwargs):
    if created:
        User.objects.create(name = instance  )
def save_user_profile(sender , instance, **kwargs):
    instance.profile.save()
    
