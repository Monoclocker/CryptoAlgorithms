from django.urls import path
import CryptoAlgorithms.views.rng_views as rng_views

urlpatterns = [
    path('', rng_views.index),
    path('chart', rng_views.get_chart),
    path('index', rng_views.index),
    path('generator/create', rng_views.create_generator),
    path('generator/generate', rng_views.generate_number),
    path('generator/save', rng_views.save_key),
    path('generator/load', rng_views.load_key),
    path('generator/generate-sequence', rng_views.generate_sequence),
    path('generator/download-sequence', rng_views.download_sequence),
    path('generator/encrypt', rng_views.execute_encryption),
    path('generator/download-encrypted', rng_views.download_encrypted_text)
]
