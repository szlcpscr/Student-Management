# Generated by Django 2.0.4 on 2018-06-22 11:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sems', '0019_provimet_refuzuar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='provimet',
            name='times',
        ),
        migrations.AlterField(
            model_name='provimet',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
