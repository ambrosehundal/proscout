# Generated by Django 3.1.5 on 2021-01-30 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scout', '0008_auto_20210130_0228'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]