from django.shortcuts import render, redirect
from .models import *
import math
import random
import string
from jdatetime import datetime as jdatetime
from jdatetime import timedelta
# Create your views here.


def token_generate():
	ran = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k = 6))
	discount_code = 'kadec'+ran
	return(discount_code)


def index(request):
    if 'token' in request.session:
        user = UserProfile.objects.filter(user_token=request.session['token']).first()
        context = {
            'games': Games.objects.all(),
            'seassons': Seassons.objects.all(),
            'profile': user,
            'statistic': UserForm.objects.all(), 
            'user_guess': UserForm.objects.filter(user=user), 
        
        }
        if request.method == 'POST':
            match_id = request.POST.get('match')
            first_game = request.POST.get('first_team')
            second_team = request.POST.get('second_team')
            match_guess = UserForm.objects.filter(game__id=match_id)
            game = Games.objects.get(id=match_id)
            if game.is_enable == True:
                current_jalali_datetime = jdatetime.now()
                game_date_time = game.date_time
                check_time = game_date_time - timedelta(minutes=15)
                if current_jalali_datetime > check_time:
                    game.is_enable = False
                    game.save()
                    context['disable_match'] = True
                else:
                    if match_guess.count() > 0:
                        match_guess = match_guess.first()
                        if first_game is not None:
                            match_guess.first_team = first_game
                            match_guess.save()
                        if second_team is not None:
                            match_guess.second_team = second_team
                            match_guess.save()
                    else:
                        UserForm.objects.create(user=user, game=game, first_team=first_game, second_team=second_team)
                    return redirect('index')
        return render(request, 'index.html', context)
    else:
        return redirect('login')

def login(request):
    if 'token' in request.session:
        return redirect('index')
    else:
        if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            department = request.POST.get('department')
            token = token_generate()
            profile = UserProfile.objects.filter(phone=phone)
            if profile.count() > 0:
                profile.first().user_token = token
                request.session['token'] = token
                return redirect('index')
            else:
                UserProfile.objects.create(name=name, phone=phone,department=department, user_token=token)
                request.session['token'] = token
                return redirect('index')
    return render(request, 'login.html', {})


def reward_calculation(request):
    context = {
        
    }    

    return render(request, 'reward.html', context)