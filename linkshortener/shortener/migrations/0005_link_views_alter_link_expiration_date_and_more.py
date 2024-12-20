# Generated by Django 5.1.3 on 2024-12-04 16:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0004_link_expiration_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='link',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 11, 16, 2, 48, 347714, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='link',
            name='shortened_url',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
