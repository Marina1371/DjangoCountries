from django.shortcuts import render
import json


def index(request):
    with open('country.json') as json_countries:
        data = json.load(json_countries)
    return render(request, 'pages/index.html', {"countries": data})


def country(request, name):
    with open('country.json') as json_countries:
        data = json.load(json_countries)
        country = [x for x in data if x['country'] == name]

        return render(request, 'pages/country.html',{
            "country": country[0]
        })


def country_list(request):
    with open('country.json') as json_countries:
        countries = json.load(json_countries)
        return render(request, 'pages/countries.html',
          {"countries": countries}
        )


def languages(request):
    languages = []

    with open('country.json') as json_countries:
        data = json.load(json_countries)

    for country in data:
        for l in country["languages"]:
            if not l in languages:
                languages.append(l)

    return render(request, 'pages/languages.html',{
        "languages": languages
    })