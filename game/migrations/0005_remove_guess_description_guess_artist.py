# Generated by Django 4.1.7 on 2023-03-25 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_guess_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guess',
            name='description',
        ),
        migrations.AddField(
            model_name='guess',
            name='artist',
            field=models.CharField(default='Unknown', max_length=255),
        ),
    ]