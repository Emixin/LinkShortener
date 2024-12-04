from django.db import models
from django.utils import timezone
import random
import string


# Create your models here.


class Link(models.Model):
    url = models.URLField()
    shortened_url = models.CharField(max_length=10, unique=True, blank=True)
    expiration_date = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=7))

    def is_expired(self):
        return self.expiration_date < timezone.now()
    
    def create_short_url(self):
        base_url = ''.join(self.url.split('/', 3)[1:3])
        base_url = 'https://' + base_url
        shortened = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(6)])
        return base_url + '/' + shortened