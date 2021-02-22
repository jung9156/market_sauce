from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    profileimage = models.URLField(null=True)
    followers = models.ManyToManyField("self")
    following = models.ManyToManyField("self")

    class Meta:
        db_table = 'account_profile'
        app_label = 'account' # <- account 앱 카테고리에서 관리되도록 한다.