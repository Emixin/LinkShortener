# Generated by Django 5.1.3 on 2024-12-04 12:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_remove_link_expiration_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 11, 12, 8, 1, 337250, tzinfo=datetime.timezone.utc)),
        ),
    ]