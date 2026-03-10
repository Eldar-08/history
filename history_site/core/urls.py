from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('stone-age/', views.stone_age, name='stone_age'),
    path('middle-ages/', views.middle_ages, name='middle_ages'),
    path('register/', views.register, name='register'),
    path('api/recommendations/', views.api_recommendations, name='api_recommendations'),
    # login/logout are provided by django.contrib.auth.urls under /accounts/
]