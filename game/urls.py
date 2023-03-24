
from django.urls import path
from django.views.generic import TemplateView
from .views import GameView


urlpatterns = [
    path('<slug:slug>', GameView.as_view(), name='index_category'),
    path('', GameView.as_view(), name='index'),
]