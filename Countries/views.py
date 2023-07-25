import json

from django.shortcuts import render


def index(request):
    # read json
    with open('country.json') as json_countries:
        data = json.load(json_countries)
        return render(request, 'pages/index.html', {"countries": data})



