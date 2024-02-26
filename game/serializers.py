# game/serializers.py
from rest_framework import serializers
from .models import Game, Guess

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'player', 'target_word', 'is_active']

class GuessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guess
        fields = ['game', 'word', 'similarity_score']
