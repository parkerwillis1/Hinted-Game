# apps.py
from django.apps import AppConfig
from .utils.glove_loader import GloVeLoader
from django.conf import settings

class GameConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'game'

    def ready(self):
        # Path to your GloVe file
        glove_file_path = str(settings.BASE_DIR / 'glove_data/glove.6B.50d.txt')
        self.glove_loader = GloVeLoader(glove_file_path)
        print("GloVe model loaded!")

