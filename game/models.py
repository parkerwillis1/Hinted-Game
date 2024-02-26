from django.db import models

# game/models.py
from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Game(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    target_word = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

class Guess(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    word = models.CharField(max_length=100)
    similarity_score = models.FloatField()

