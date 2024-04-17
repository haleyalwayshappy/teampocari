from django.shortcuts import render

from django.http import HttpResponse
from home.models import Portfolio


def index(request):
    context = dict()
    # 각 필드 값에 따라 분류
    context['enterprise_portfolios'] = Portfolio.objects.filter(field=1)
    context['product_portfolios'] = Portfolio.objects.filter(field=2)
    context['vlog_portfolios'] = Portfolio.objects.filter(field=3)

    return render(request, "home/index.html", context)