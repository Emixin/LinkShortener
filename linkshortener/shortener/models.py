from django.db import models
from django.utils import timezone
import random
import string




class Link(models.Model):
    url = models.URLField()
    shortened_url = models.CharField(max_length=10, unique=True)
    expiration_date = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=7))
    views = models.PositiveIntegerField(default=0)

    def is_expired(self):
        return self.expiration_date < timezone.now()
    
    def set_short_url(self):
        shortened = ''.join([random.choice(string.ascii_letters) for _ in range(6)])
        self.shortened_url = shortened

    def increase_views(self):
        self.views += 1
        self.save()