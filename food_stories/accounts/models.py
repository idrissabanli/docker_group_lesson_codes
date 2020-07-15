from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    image = models.ImageField(upload_to='user_images', null=True, blank=True)
    bio = models.TextField(_('Biography'), null=True, blank=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_avatar(self):
        if self.image:
            return self.image.url
        return 'https://cdt.org/files/2015/10/2015-10-06-FB-person.png'

    @property
    def is_author(self):
        return self.groups.filter(name='author').exists()
