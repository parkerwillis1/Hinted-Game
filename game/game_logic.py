# game/game_logic.py
from .models import Game, Guess
from .utils.glove_loader import GloVeLoader
from django.apps import apps

class GameManager:

    @staticmethod
    def start_new_game(player):
        # Placeholder for word selection logic
        target_word = 'coffee'  
        game = Game.objects.create(player=player, target_word=target_word)
        return game

    @staticmethod
    def get_game(game_id):
        return Game.objects.get(id=game_id)

class GameSession:

    def __init__(self, game):
        self.game = game
        self.glove_loader = apps.get_app_config('game').glove_loader

    def make_guess(self, guess_word):
        # Compute similarity and other game logic
        target_vector = self.glove_loader.get_word_vector(self.game.target_word)
        guess_vector = self.glove_loader.get_word_vector(guess_word)
        similarity = self.compute_similarity(target_vector, guess_vector)
        Guess.objects.create(game=self.game, word=guess_word, similarity_score=similarity)
        return similarity

    def compute_similarity(self, vec1, vec2):
        # Implement cosine similarity or another metric
        pass
