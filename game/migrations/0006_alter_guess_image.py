# Generated by Django 4.1.7 on 2023-03-25 15:54

from django.db import migrations, models
import game.models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_remove_guess_description_guess_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guess',
            name='image',
            field=models.ImageField(upload_to=game.models.update_filename),
        ),
    ]