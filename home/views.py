from django.shortcuts import render

from django.http import HttpResponse
from home.models import portfolio


def index(request):
    context = dict()
    portfolios = portfolio.objects.all()

    context["portfolios"] = portfolios

    print(context)
    return render(request, "home/index.html",context = context )
