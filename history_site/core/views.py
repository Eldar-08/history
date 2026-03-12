from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import JsonResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
import requests

from .models import HistoricalFact, Comment, SavedArticle, HistoricalPeriod


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


def fact_list(request):
    facts = HistoricalFact.objects.select_related('period').all()
    if not facts.exists():
        # create some default periods and facts for demo
        stone, _ = HistoricalPeriod.objects.get_or_create(
            name='stone',
            defaults={'start_year': -3000000, 'end_year': -3000,
                      'description': 'Период доисторических охотников-собирателей.'}
        )
        medieval, _ = HistoricalPeriod.objects.get_or_create(
            name='medieval',
            defaults={'start_year': 500, 'end_year': 1500,
                      'description': 'Эпоха тюркских каганатов и монгольских завоеваний.'}
        )
        HistoricalFact.objects.create(
            title='Появление человека в регионе',
            description='Археологические находки указывают на обитание человека в современных границах Кыргызстана уже в каменном веке.',
            period=stone,
            year=-1500000
        )
        HistoricalFact.objects.create(
            title='Монгольское завоевание',
            description='В начале XIII века земли тюркских каганатов были завоёваны войсками Чингисхана.',
            period=medieval,
            year=1219
        )
        facts = HistoricalFact.objects.select_related('period').all()
    return render(request, 'core/fact_list.html', {'facts': facts})


def fact_detail(request, pk):
    fact = get_object_or_404(HistoricalFact, pk=pk)
    fact.views += 1
    fact.save(update_fields=['views'])
    comments = fact.comments.select_related('author').all()
    is_saved = False
    if request.user.is_authenticated:
        is_saved = SavedArticle.objects.filter(user=request.user, fact=fact).exists()
    return render(request, 'core/fact_detail.html', {'fact': fact, 'comments': comments, 'is_saved': is_saved})


@login_required
def add_comment(request, pk):
    fact = get_object_or_404(HistoricalFact, pk=pk)
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            Comment.objects.create(fact=fact, author=request.user, text=text)
    return redirect('fact_detail', pk=pk)


@login_required
def toggle_save_fact(request, pk):
    fact = get_object_or_404(HistoricalFact, pk=pk)
    saved, created = SavedArticle.objects.get_or_create(user=request.user, fact=fact)
    if not created:
        saved.delete()
    return redirect('fact_detail', pk=pk)


@login_required
def saved_facts(request):
    saved = SavedArticle.objects.filter(user=request.user).select_related('fact')
    return render(request, 'core/saved_facts.html', {'saved': saved})