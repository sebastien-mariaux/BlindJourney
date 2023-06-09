import os
import uuid
from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.utils.safestring import mark_safe


def update_filename(instance, _):
    path = ""
    return os.path.join(path, str(uuid.uuid4())
                        )


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

    def guesses_count(self):
        return self.guesses.count()


class Guess(models.Model):
    prompt = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    image = models.ImageField(
        null=False,
        blank=False,
        upload_to=update_filename
    )
    artist = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        default='Unknown',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='guesses',
        null=False,
        blank=False
    )
    attempts_count = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )
    correct_count = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )

    class Meta:
        verbose_name = 'guess'
        verbose_name_plural = 'guesses'

    def __str__(self):
        return str(self.prompt)

    def success_ratio(self):
        if self.attempts_count == 0:
            return 0
        return round(self.correct_count / self.attempts_count, 2)

    @property
    def difficulty(self):
        if self.success_ratio() > 0.8:
            return 0
        if self.success_ratio() > 0.6:
            return 1
        if self.success_ratio() > 0.4:
            return 2
        if self.success_ratio() > 0.2:
            return 3
        return 4

    @property
    def difficulty_label(self):
        return {
            0: 'Easy',
            1: 'Medium',
            2: 'Hard',
            3: 'Very Hard',
            4: 'Impossible'
        }[self.difficulty]

    def save_good_guess(self):
        self.correct_count += 1
        self.attempts_count += 1
        self.save()

    def save_bad_guess(self):
        self.attempts_count += 1
        self.save()

    def img_preview(self):
        return mark_safe('<img src = "{url}" width = "300"/>'.format(
            url=self.image.url
        ))

    def img_thumbnail(self):
        return mark_safe('<img src = "{url}" width = "50"/>'.format(
            url=self.image.url
        ))
