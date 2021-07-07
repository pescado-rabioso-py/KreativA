from django.shortcuts import render, HttpResponse
from .models import Home, About, Profile, Category, Portfolio, Slider #Skills
# Create your views here.

def index(request):
    #Home
    home = Home.objects.latest('updated')

    #About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)

    #Skills
    categories = Category.objects.all()

    #Portfolio
    portfolios = Portfolio.objects.all()

    #Slider
    slider = Slider.objects.all()
    
    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios,
        'sliders': slider
    }

    return render(request, 'index.html', context)

'''def portfolio(request):
    portfolios = Portfolio.objects.all()
    context = {"portfolios": portfolios}
    return render(request, 'portfolios.html', context)'''

def details(request, slug_details):
    portfolios = Portfolio.objects.all()
    portfolio = Portfolio.objects.filter(slug=slug_details)
    if portfolio.exists():
        portfolio = portfolio.first()
    else:
        return HttpResponse("<h1>A tomar viento que no existe tal página</h1>")

    context = {'portfolios':portfolios, 'details': details}

    return render(request, 'details.html', context)

