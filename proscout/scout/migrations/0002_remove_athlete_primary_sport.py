# Generated by Django 2.2.7 on 2020-11-11 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='athlete',
            name='primary_sport',
        ),
    ]
