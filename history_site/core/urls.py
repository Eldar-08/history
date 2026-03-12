from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('stone-age/', views.stone_age, name='stone_age'),
    path('middle-ages/', views.middle_ages, name='middle_ages'),
    path('register/', views.register, name='register'),
    path('api/recommendations/', views.api_recommendations, name='api_recommendations'),

    # facts CRUD
    path('facts/', views.fact_list, name='fact_list'),
    path('facts/<int:pk>/', views.fact_detail, name='fact_detail'),
    path('facts/<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('facts/<int:pk>/save/', views.toggle_save_fact, name='toggle_save_fact'),
    path('saved/', views.saved_facts, name='saved_facts'),

    # login/logout are provided by django.contrib.auth.urls under /accounts/
]