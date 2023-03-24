from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Guess
from django.db.models import Count


class GameView(TemplateView):
    template_name = 'game/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = kwargs.get('slug')
        context['category'] = category
        context['guess'] = self.random_guess(category)
        return context

    def random_guess(self, category):
        if category:
            return Guess.objects.filter(category__slug=category).order_by('?').first()
        else:
            return Guess.objects.order_by('?').first()
