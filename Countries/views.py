from django.shortcuts import render


def index(request):
    return render(request, 'pages/app.html')



