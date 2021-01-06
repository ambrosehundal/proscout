# Generated by Django 2.2.7 on 2021-01-06 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scout', '0002_remove_athlete_primary_sport'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Athlete',
        ),
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='height',
            field=models.IntegerField(default=72),
        ),
        migrations.AddField(
            model_name='profile',
            name='hometown',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='weight',
            field=models.IntegerField(default=180),
        ),
        migrations.AlterField(
            model_name='profile',
            name='headline',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='profile',
            name='summary',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]