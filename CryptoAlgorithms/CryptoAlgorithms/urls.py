from django.urls import path
import CryptoAlgorithms.views.rng_views as rng_views

urlpatterns = [
    path('', rng_views.index),
    path('chart', rng_views.get_chart),
    path('index', rng_views.index),
    path('generator/create', rng_views.create_generator),
    path('generator/generate', rng_views.generate_number)
]
