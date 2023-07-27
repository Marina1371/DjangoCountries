from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Country, Language


def index(request):
    countries = Country.objects.order_by('country_name').all()
    return render(request, 'pages/index.html', {
        "countries": countries
    })


def country(request, name):
    country = Country.objects.get(country_name=name)
    langs = country.langs.all()
    return render(request, 'pages/country.html', {
        "country": country, "langs": langs
    })


def country_list(request):
    page_number = request.GET.get('page')
    letters = []
    countries = Country.objects.order_by('country_name').all()
    for country in countries:
        if country.country_name[0] not in letters:
            letters.append(country.country_name[0])
    paginator = Paginator(countries, 10)
    page_obj = paginator.get_page(page_number)
    return render(request, 'pages/countries.html', {
        "countries": countries,
        "letters": letters,
        "page_obj": page_obj
    })


def languages(request):
    languages = Language.objects.order_by('name').all()
    return render(request, 'pages/languages.html', {
        "languages": languages
    })


def language(request, name):
    language = Language.objects.get(name=name)
    countries = Country.objects.filter(langs=language)
    return render(request, 'pages/language.html', {
        "language": name,
        "countries": countries
    })


def countries_letter(request, letter):
    countries = Country.objects.filter(country_name__startswith=letter)
    return render(request, 'pages/countries_by_letter.html', {
        "letter": letter,
        "countries": countries
    })