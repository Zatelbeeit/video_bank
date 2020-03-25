from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from userena.models import UserenaBaseProfile



# Create your models here.


class MyProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='my_profile',
                                on_delete=models.CASCADE)

    