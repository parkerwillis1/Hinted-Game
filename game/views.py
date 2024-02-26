from django.shortcuts import render

# game/views.py
from django.http import JsonResponse
from .game_logic import GameManager
from .models import Player

def start_game(request):
    # This could be expanded to handle user sessions, etc.
    player = Player.objects.get_or_create(username='player1')[0]
    game = GameManager.start_new_game(player)
    return JsonResponse({'game_id': game.id, 'message': 'Game started'})

def make_guess(request):
    # Placeholder: Extract guess and game_id from the request
    guess = request.GET.get('guess')
    game_id = request.GET.get('game_id')

    game = GameManager.get_game(game_id)
    result = game.make_guess(guess)
    return JsonResponse({'result': result})

def sample_api(request):
    data = {'message': 'Hello from Django!'}
    return JsonResponse(data)

