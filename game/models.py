from django.db import models
from django_extensions.db.fields import AutoSlugField


class Category(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False
    )
    slug = AutoSlugField(
        populate_from="name",
        max_length=255,
        unique=True,
        null=False,
        blank=False
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Guess(models.Model):
    prompt = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    image = models.ImageField(
        null=False,
        blank=False
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='guesses',
        null=False,
        blank=False
    )

    class Meta:
        verbose_name = 'guess'
        verbose_name_plural = 'guesses'

    def __str__(self):
        return str(self.prompt)
