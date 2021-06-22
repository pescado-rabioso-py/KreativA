from django.shortcuts import render
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
