from django.urls import path
from . import views
from django.contrib import admin
app_name='NewsUpdates'
urlpatterns=[
    path('',views.HomeView,name='Home'),
    path('About/',views.AboutView,name='About'),
    path('AutoMobileNews/',views.AutoMobileDetailView,name='AutoMobileNews'),
    path('TechnologyNews/',views.TechnologyDetailView,name='TechnologyNews'),
    path('EducationNews/',views.EducationDetailView,name='EducationNews'),
    path('CrimeNews/',views.CrimeDetailView,name='CrimeNews'),
    path('BusinessNews/',views.BusinessDetailView,name='BusinessNews'),
    path('CryptoCurrencyNews/',views.CryptoCurrencyDetailView,name='Crypto-CurrencyNews'),
    path('HealthNews/',views.HealthDetailView,name='HealthNews'),
    path('FilmNews/',views.FilmDetailView,name='Film-News'),
    path('ScienceNews/',views.ScienceDetailView,name='Science-News'),
    path('SportsNews/',views.SportsDetailView,name='Sports-News'),
    path('FoodVarietyNews/',views.FoodVarietyDetailView,name='FoodvarietyNews'),
    path('LifeStyleNews/',views.LifeStyleDetailView,name='LifeStyleNews'),
    path('SearchNews/',views.SearchView,name='Search-Details'),
    path('FeedbackDetails/',views.FeedbackView,name='FeedBackDetails'),
]