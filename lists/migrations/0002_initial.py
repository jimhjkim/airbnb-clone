# Generated by Django 4.0.1 on 2022-01-16 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lists', '0001_initial'),
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='rooms',
            field=models.ManyToManyField(blank=True, to='rooms.Room'),
        ),
    ]
