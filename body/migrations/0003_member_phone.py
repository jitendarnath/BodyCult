# Generated by Django 2.2.6 on 2019-12-01 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('body', '0002_workout_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]
