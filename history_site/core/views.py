from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import JsonResponse
import requests


def home(request):
    # render homepage with template
    return render(request, 'core/home.html')


def stone_age(request):
    return render(request, 'core/stone_age.html')


def middle_ages(request):
    return render(request, 'core/middle_ages.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Пользователь {username} успешно зарегистрирован. Теперь можно войти.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})


def api_recommendations(request):
    # Simple API to recommend related topics from external sources
    recommendations = [
        {
            "title": "История Кыргызстана на Википедии",
            "url": "https://en.wikipedia.org/wiki/History_of_Kyrgyzstan",
            "description": "Подробная статья о истории Кыргызстана от древних времен до наших дней."
        },
        {
            "title": "Каменный век в Центральной Азии",
            "url": "https://en.wikipedia.org/wiki/Prehistoric_Central_Asia",
            "description": "Информация о доисторических периодах в регионе."
        },
        {
            "title": "Средневековая история тюркских народов",
            "url": "https://en.wikipedia.org/wiki/Turkic_peoples",
            "description": "О тюркских каганатах и их влиянии."
        }
    ]
    return JsonResponse({"recommendations": recommendations})