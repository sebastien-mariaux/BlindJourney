# Generated by Django 4.1.7 on 2023-03-24 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_guess_attempts_count_guess_correct_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='guess',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
