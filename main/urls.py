from . import views
from django.urls import path

from .views import SearchResultsView, SearchResultsViewauto

urlpatterns = [path('', views.main, name="index"),
               path('human/', views.human, name="human"),
               path('search/', SearchResultsView, name='search_results'),
               path('auto/', views.auto, name="human"),
               path('search_auto/', SearchResultsViewauto, name='search_results_auto'),
               ]
