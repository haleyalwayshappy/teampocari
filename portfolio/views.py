from django.shortcuts import render
from django.http import HttpResponse
from home.models import portfolio

def index(request):
    context = dict()
    portfolios = portfolio.objects.all()
    context["portfolios"] = portfolios

    return render(request, "portfolio/index.html",context=context )
