from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    # return HttpResponse("<h2>홈 호하면  </h2>")
    return render(request, "home/index.html", )
