# Generated by Django 4.0.4 on 2022-05-07 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetup',
            name='location',
        ),
    ]
