
from django.urls import path
from django.views.generic import TemplateView
from .views import GameView


urlpatterns = [
    path('', GameView.as_view(), name='index'),
]
