# Generated by Django 2.2.7 on 2021-01-09 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scout', '0003_auto_20210106_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='disciplines',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
