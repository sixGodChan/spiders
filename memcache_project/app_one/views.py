from django.shortcuts import render, HttpResponse
import time

from django.views.decorators.cache import cache_page


@cache_page(5)
def index(request):
    return render(request, 'index.html', {'time': time.time()})


def foo(request):
    return render(request, 'foo.html', {'time': time.time()})


def fff(request):
    ctime = time.time()
    return HttpResponse(ctime)
