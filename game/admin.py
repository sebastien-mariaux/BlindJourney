from django.contrib import admin
from .models import Category, Guess


class CategoryAdmin(admin.ModelAdmin):
        list_display = ('name', 'slug', 'guesses_count')



class GuessAdmin(admin.ModelAdmin):
    list_display = ('prompt', 'artist', 'category', 'image', 'attempts_count', 'correct_count', 'img_thumbnail')
    fields = ('prompt', 'artist', 'category', 'image', 'img_preview')
    readonly_fields = ['img_preview']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Guess, GuessAdmin)
