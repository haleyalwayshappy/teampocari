from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse("<h2>포트폴리오사이트 </h2>")
    return render(request, "portfolio/index.html", )
