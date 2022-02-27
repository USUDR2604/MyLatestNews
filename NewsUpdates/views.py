from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from NewsUpdates.forms import FeedbackForm
from newsapi import NewsApiClient
from django.db.models import Q  # New
from datetime import date
from datetime import timedelta
from MyLatestNews.settings import *
import datetime
import random
from .Choices import *
# Past Days
past_day=date.today()-timedelta(days=1)
future_day=date.today()+timedelta(days=1)
#Current Time
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
# SQL CONNECTOR

# Create your views here.


def HomeView(request):
    return render(request,'NewsUpdates/Home.html',{})

def AboutView(request):
    return render(request,'NewsUpdates/About.html',{})

def FeedbackView(request):
    context ={}
    form = FeedbackForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        # save the form data to model
        form.save()
    context['form']= form
    return render(request, "NewsUpdates/FeedbackForm.html", context)

def SearchView(request):
    search_item=request.GET.get('search')
    AutoMobile_newslis=[]
    if search_item:
        newsapi = NewsApiClient(api_key =SECRET_KEY_3) 
        # Business News
        AutoMobileNews= newsapi.get_everything(q=search_item,from_param=past_day,to=future_day,language='en')
        AutoMobile_news = AutoMobileNews['articles'] 
        for i in AutoMobile_news:
            AutoMobile_newslis.append({
            "Category":search_item,
            "title": i["title"],
            "description": i["description"],
            "url": i["url"],
            "image": i["urlToImage"] if i["urlToImage"] is not None else AutoMobiles['ImageUrl'],
            "publishedat": i["publishedAt"].split('T')[0],
            "publishtime": i["publishedAt"].split("T")[1][:-1],
        })
        print(len(AutoMobile_newslis))
        s_name=str(search_item)
        item_name=s_name.upper()+str(" NEWS")
        return render(request,'NewsUpdates/SearchItemNews.html',{'AutoMobile_newslis':AutoMobile_newslis,'item_name':item_name})
    else:
        return render(request,'NewsUpdates/SearchItemNews.html',{'AutoMobile_newslis':AutoMobile_newslis})

def AutoMobileDetailView(request):
    try:
        newsapi = NewsApiClient(api_key =SECRET_KEY_1) 
        # Business News
        AutoMobile_newslis=[]
        AutoMobileNews= newsapi.get_everything(q='AutoMobile',from_param=past_day,to=future_day,language='en')
        AutoMobile_news = AutoMobileNews['articles'] 
        for i in AutoMobile_news:
            AutoMobile_newslis.append({
            "Category":"AUTOMOBILES",
            "title": i["title"],
            "description": i["description"],
            "url": i["url"],
            "image": i["urlToImage"] if i["urlToImage"] is not None else AutoMobiles['ImageUrl'],
            "publishedat": i["publishedAt"].split('T')[0],
            "publishtime": i["publishedAt"].split("T")[1][:-1],
        })
        benz_newslis=[]
        benzNews= newsapi.get_everything(q='benz',from_param=past_day,to=future_day,language='en')
        benz_news = benzNews['articles'] 
        for i in benz_news:
            benz_newslis.append({
            "Category":"Benz",
            "title": i["title"],
            "description": i["description"],
            "url": i["url"],
            "image": i["urlToImage"],
            "publishedat": i["publishedAt"].split('T')[0],
            "publishtime": i["publishedAt"].split("T")[1][:-1],
        })
        random.shuffle(benz_newslis)
        print("kk")
        return render(request,'NewsUpdates/Categories/AutoMobiles/AutoMobileDetails.html',{'AutoMobile_newslis':AutoMobile_newslis,'benz_newslis':benz_newslis})
    except:
        print("Error")

def TechnologyDetailView(request):
    try:
        newsapi = NewsApiClient(api_key =SECRET_KEY_1) 
        # Business News
        Technology_newslis=[]
        TechnologyNews= newsapi.get_everything(q='Technology',from_param=past_day,to=future_day,language='en')
        Technology_news = TechnologyNews['articles'] 
        for i in Technology_news:
            Technology_newslis.append({
            "Category":"Technology",
            "title": i["title"],
            "description": i["description"],
            "url": i["url"],
            "image": i["urlToImage"],
            "publishedat": i["publishedAt"].split('T')[0],
            "publishtime": i["publishedAt"].split("T")[1][:-1],
        })
        Audi_newslis=[]
        AudiNews= newsapi.get_everything(q='Audi',from_param=past_day,to=future_day,language='en')
        Audi_news = AudiNews['articles'] 
        for i in Audi_news:
            Audi_newslis.append({
            "Category":"AUDI",
            "title": i["title"],
            "description": i["description"],
            "url": i["url"],
            "image": i["urlToImage"],
            "publishedat": i["publishedAt"].split('T')[0],
            "publishtime": i["publishedAt"].split("T")[1][:-1],
        })
        random.shuffle(Audi_newslis)
        return render(request,'NewsUpdates/Categories/Technology/TechnologyDetails.html',{'Technology_newslis':Technology_newslis,'Audi_newslis':Audi_newslis})
    except:
        print("Error")

def EducationDetailView(request):
    try:
        newsapi = NewsApiClient(api_key =SECRET_KEY_1) 
        # Business News
        Education_newslis=[]
        EducationNews= newsapi.get_everything(q='Education',from_param=past_day,to=future_day,language='en')
        Education_news = EducationNews['articles'] 
        for i in Education_news:
            Education_newslis.append({
            "Category":"EDUCATION",
            "title": i["title"],
            "description": i["description"],
            "url": i["url"],
            "image": i["urlToImage"],
            "publishedat": i["publishedAt"].split('T')[0],
            "publishtime": i["publishedAt"].split("T")[1][:-1],
        })
        #Tesla Car News
        Tesla_newslis=[]
        TeslaNews= newsapi.get_everything(q='Tesla',from_param=past_day,to=future_day,language='en')
        Tesla_news = TeslaNews['articles'] 
        for i in Tesla_news:
            Tesla_newslis.append({
            "Category":"Tesla",
            "title": i["title"],
            "description": i["description"],
            "url": i["url"],
            "image": i["urlToImage"],
            "publishedat": i["publishedAt"].split('T')[0],
            "publishtime": i["publishedAt"].split("T")[1][:-1],
        })
        return render(request,'NewsUpdates//Categories/Education/EducationDet.html',{'Education_newslis':Education_newslis,'Tesla_newslis':Tesla_newslis,})
    except:
        return render(request,'NewsUpdates/ErrorTemplates/ErrorTemplate.html',{})

def CrimeDetailView(request):
    try:
        newsapi = NewsApiClient(api_key =SECRET_KEY_1) 
        # Business News
        Crime_newslis=[]
        CrimeNews= newsapi.get_everything(q='Crime',from_param=past_day,to=future_day,language='en')
        Crime_news = CrimeNews['articles'] 
        for i in Crime_news:
            Crime_newslis.append({
            "Category":"CRIME",
            "title": i["title"],
            "description": i["description"],
            "url": i["url"],
            "image": i["urlToImage"],
            "publishedat": i["publishedAt"].split('T')[0],
            "publishtime": i["publishedAt"].split("T")[1][:-1],
        })
        #Tesla Car News
        RR_newslis=[]
        RRNews= newsapi.get_everything(q='RR',from_param=past_day,to=future_day,language='en')
        RR_news = RRNews['articles'] 
        for i in RR_news:
            RR_newslis.append({
            "Category":"RR",
            "title": i["title"],
            "description": i["description"],
            "url": i["url"],
            "image": i["urlToImage"],
            "publishedat": i["publishedAt"].split('T')[0],
            "publishtime": i["publishedAt"].split("T")[1][:-1],
        })
        return render(request,'NewsUpdates/Categories/Crime/CrimeNews.html',{'Crime_newslis':Crime_newslis,'RR_newslis':RR_newslis})
    except:
        return None

def BusinessDetailView(request):
    try:
        newsapi = NewsApiClient(api_key =SECRET_KEY_1) 
        # Business News
        Business_newslis=[]
        BusinessNews= newsapi.get_everything(q='Business',from_param=past_day,to=future_day,language='en')
        Business_news = BusinessNews['articles'] 
        for i in Business_news:
            Business_newslis.append({
            "Category":"Business",
            "title": i["title"],
            "description": i["description"],
            "url": i["url"],
            "image": i["urlToImage"],
            "publishedat": i["publishedAt"].split('T')[0],
            "publishtime": i["publishedAt"].split("T")[1][:-1],
        })
        #Tesla Car News
        Stocks_newslis=[]
        StocksNews= newsapi.get_everything(q='Stocks',from_param=past_day,to=future_day,language='en')
        Stocks_news = StocksNews['articles'] 
        for i in Stocks_news:
            Stocks_newslis.append({
            "Category":"Stocks",
            "title": i["title"],
            "description": i["description"],
            "url": i["url"],
            "image": i["urlToImage"],
            "publishedat": i["publishedAt"].split('T')[0],
            "publishtime": i["publishedAt"].split("T")[1][:-1],
        })
        return render(request,'NewsUpdates/Categories/Business/BusinessNews.html',{'Business_newslis':Business_newslis,'Stocks_newslis':Stocks_newslis})
    except:
        return render(request,'NewsUpdates/ErrorTemplates/ErrorTemplate.html',{})

def CryptoCurrencyDetailView(request):
    try:
        newsapi = NewsApiClient(api_key =SECRET_KEY_1) 
        # Business News
        CryptoCurrency_newslis=[]
        CryptoCurrencyNews= newsapi.get_everything(q='Crypto-Currency',from_param=past_day,to=future_day,language='en')
        CryptoCurrency_news = CryptoCurrencyNews['articles'] 
        for i in CryptoCurrency_news:
            CryptoCurrency_newslis.append({
            "Category":"Crypto-Currency",
            "title": i["title"],
            "description": i["description"],
            "url": i["url"],
            "image": i["urlToImage"],
            "publishedat": i["publishedAt"].split('T')[0],
            "publishtime": i["publishedAt"].split("T")[1][:-1],
        })
        #Tesla Car News
        ShareMarket_newslis=[]
        ShareMarketNews= newsapi.get_everything(q='Share-Market',from_param=past_day,to=future_day,language='en')
        ShareMarket_news = ShareMarketNews['articles'] 
        for i in ShareMarket_news:
            ShareMarket_newslis.append({
            "Category":"Share Market",
            "title": i["title"],
            "description": i["description"],
            "url": i["url"],
            "image": i["urlToImage"],
            "publishedat": i["publishedAt"].split('T')[0],
            "publishtime": i["publishedAt"].split("T")[1][:-1],
        })
        return render(request,'NewsUpdates/Categories/Crypto-Currency/CryptoCurrency.html',{'CryptoCurrency_newslis':CryptoCurrency_newslis,'ShareMarket_newslis':ShareMarket_newslis})
    except:
        return render(request,'NewsUpdates/ErrorTemplates/ErrorTemplate.html',{})

def HealthDetailView(request):
    try:
        newsapi = NewsApiClient(api_key =SECRET_KEY_2) 
        # Business News
        Health_newslis=[]
        HealthNews= newsapi.get_everything(q='Health',from_param=past_day,to=future_day,language='en')
        Health_news = HealthNews['articles'] 
        for i in Health_news:
            Health_newslis.append({
            "Category":"Health",
            "title": i["title"],
            "description": i["description"],
            "url": i["url"],
            "image": i["urlToImage"],
            "publishedat": i["publishedAt"].split('T')[0],
            "publishtime": i["publishedAt"].split("T")[1][:-1],
        })
        #Tesla Car News
        Medicines_newslis=[]
        MedicinesNews= newsapi.get_everything(q='Medicines',from_param=past_day,to=future_day,language='en')
        Medicines_news = MedicinesNews['articles'] 
        for i in Medicines_news:
            Medicines_newslis.append({
            "Category":"Medicines",
            "title": i["title"],
            "description": i["description"],
            "url": i["url"],
            "image": i["urlToImage"],
            "publishedat": i["publishedAt"].split('T')[0],
            "publishtime": i["publishedAt"].split("T")[1][:-1],
        })
        return render(request,'NewsUpdates/Categories/Health/HealthNews.html',{'Health_newslis':Health_newslis,'Medicines_newslis':Medicines_newslis})
    except:
        return render(request,'NewsUpdates/ErrorTemplates/ErrorTemplate.html',{})

def FilmDetailView(request):
    try:
        newsapi = NewsApiClient(api_key =SECRET_KEY_2) 
        # Business News
        Movies_newslis=[]
        MoviesNews= newsapi.get_everything(q='Movies',from_param=past_day,to=future_day,language='en')
        Movies_news = MoviesNews['articles'] 
        for i in Movies_news:
            Movies_newslis.append({
            "Category":"Movies",
            "title": i["title"],
            "description": i["description"],
            "url": i["url"],
            "image": i["urlToImage"],
            "publishedat": i["publishedAt"].split('T')[0],
            "publishtime": i["publishedAt"].split("T")[1][:-1],
        })
        #Tesla Car News
        FilmIndustry_newslis=[]
        FilmIndustryNews= newsapi.get_everything(q='Film-Industry',from_param=past_day,to=future_day,language='en')
        FilmIndustry_news = FilmIndustryNews['articles'] 
        for i in FilmIndustry_news:
            FilmIndustry_newslis.append({
            "Category":"Film-Industry",
            "title": i["title"],
            "description": i["description"],
            "url": i["url"],
            "image": i["urlToImage"],
            "publishedat": i["publishedAt"].split('T')[0],
            "publishtime": i["publishedAt"].split("T")[1][:-1],
        })
        return render(request,'NewsUpdates/Categories/Films/FilmIndustryNews.html',{'Movies_newslis':Movies_newslis,'FilmIndustry_newslis':FilmIndustry_newslis})
    except:
        return render(request,'NewsUpdates/ErrorTemplates/ErrorTemplate.html',{})

def SportsDetailView(request):
    try:
        newsapi = NewsApiClient(api_key =SECRET_KEY_2) 
        # Business News
        Sports_newslis=[]
        SportsNews= newsapi.get_everything(q='Sports',from_param=past_day,to=future_day,language='en')
        Sports_news = SportsNews['articles'] 
        for i in Sports_news:
            Sports_newslis.append({
            "Category":"Sports",
            "title": i["title"],
            "description": i["description"],
            "url": i["url"],
            "image": i["urlToImage"],
            "publishedat": i["publishedAt"].split('T')[0],
            "publishtime": i["publishedAt"].split("T")[1][:-1],
        })
        #Tesla Car News
        Cricket_newslis=[]
        CricketNews= newsapi.get_everything(q='Cricket',from_param=past_day,to=future_day,language='en')
        Cricket_news = CricketNews['articles'] 
        for i in Cricket_news:
            Cricket_newslis.append({
            "Category":"Cricket",
            "title": i["title"],
            "description": i["description"],
            "url": i["url"],
            "image": i["urlToImage"],
            "publishedat": i["publishedAt"].split('T')[0],
            "publishtime": i["publishedAt"].split("T")[1][:-1],
        })
        return render(request,'NewsUpdates/Categories/Sports/SportsDetails.html',{'Sports_newslis':Sports_newslis,'Cricket_newslis':Cricket_newslis})
    except:
        return render(request,'NewsUpdates/ErrorTemplates/ErrorTemplate.html',{})

def ScienceDetailView(request):
    try:
        newsapi = NewsApiClient(api_key =SECRET_KEY_2) 
        # Business News
        Science_newslis=[]
        ScienceNews= newsapi.get_everything(q='Science',from_param=past_day,to=future_day,language='en')
        Science_news = ScienceNews['articles'] 
        for i in Science_news:
            Science_newslis.append({
            "Category":"Science",
            "title": i["title"],
            "description": i["description"],
            "url": i["url"],
            "image": i["urlToImage"],
            "publishedat": i["publishedAt"].split('T')[0],
            "publishtime": i["publishedAt"].split("T")[1][:-1],
        })
        #Tesla Car News
        Chemist_newslis=[]
        ChemistNews= newsapi.get_everything(q='Chemist',from_param=past_day,to=future_day,language='en')
        Chemist_news = ChemistNews['articles'] 
        for i in Chemist_news:
            Chemist_newslis.append({
            "Category":"Chemist",
            "title": i["title"],
            "description": i["description"],
            "url": i["url"],
            "image": i["urlToImage"],
            "publishedat": i["publishedAt"].split('T')[0],
            "publishtime": i["publishedAt"].split("T")[1][:-1],
        })
        return render(request,'NewsUpdates/Categories/Science/ScienceNews.html',{'Science_newslis':Science_newslis,'Chemist_newslis':Chemist_newslis})
    except:
        return render(request,'NewsUpdates/ErrorTemplates/ErrorTemplate.html',{})

def FoodVarietyDetailView(request):
    try:
        newsapi = NewsApiClient(api_key =SECRET_KEY_2) 
        # Business News
        FoodVariety_newslis=[]
        FoodVarietyNews= newsapi.get_everything(q='Food-Variety',from_param=past_day,to=future_day,language='en')
        FoodVariety_news = FoodVarietyNews['articles'] 
        for i in FoodVariety_news:
            FoodVariety_newslis.append({
            "Category":"Food Varietys",
            "title": i["title"],
            "description": i["description"],
            "url": i["url"],
            "image": i["urlToImage"],
            "publishedat": i["publishedAt"].split('T')[0],
            "publishtime": i["publishedAt"].split("T")[1][:-1],
        })
        #Tesla Car News
        Restaurants_newslis=[]
        RestaurantsNews= newsapi.get_everything(q='Restaurants',from_param=past_day,to=future_day,language='en')
        Restaurants_news = RestaurantsNews['articles'] 
        for i in Restaurants_news:
            Restaurants_newslis.append({
            "Category":"Restaurant",
            "title": i["title"],
            "description": i["description"],
            "url": i["url"],
            "image": i["urlToImage"],
            "publishedat": i["publishedAt"].split('T')[0],
            "publishtime": i["publishedAt"].split("T")[1][:-1],
        })
        print("Details Ready")
        return render(request,'NewsUpdates/Categories/Food-Variety/Food_VarietyNews.html',{'FoodVariety_newslis':FoodVariety_newslis,'Restaurants_newslis':Restaurants_newslis})
    except:
        return None

def LifeStyleDetailView(request):
    try:
        newsapi = NewsApiClient(api_key =SECRET_KEY_2) 
        # Business News
        LifeStyle_newslis=[]
        LifeStyleNews= newsapi.get_everything(q='Life-Style',from_param=past_day,to=future_day,language='en')
        LifeStyle_news = LifeStyleNews['articles'] 
        for i in LifeStyle_news:
            LifeStyle_newslis.append({
            "Category":"Life Style",
            "title": i["title"],
            "description": i["description"],
            "url": i["url"],
            "image": i["urlToImage"],
            "publishedat": i["publishedAt"].split('T')[0],
            "publishtime": i["publishedAt"].split("T")[1][:-1],
        })
        #Tesla Car News
        Style_newslis=[]
        StyleNews= newsapi.get_everything(q='Style',from_param=past_day,to=future_day,language='en')
        Style_news = StyleNews['articles'] 
        for i in Style_news:
            Style_newslis.append({
            "Category":"Style",
            "title": i["title"],
            "description": i["description"],
            "url": i["url"],
            "image": i["urlToImage"],
            "publishedat": i["publishedAt"].split('T')[0],
            "publishtime": i["publishedAt"].split("T")[1][:-1],
        })
        return render(request,'NewsUpdates/Categories/Life-Style/LifeStyleNews.html',{'LifeStyle_newslis':LifeStyle_newslis,'Style_newslis':Style_newslis})
    except:
        return render(request,'NewsUpdates/ErrorTemplates/ErrorTemplate.html',{})

