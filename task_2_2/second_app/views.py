from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.


def index_test(request):
    return HttpResponse('<h1>Hello</h1>')


def render_test(request):
    return render(request, 'render_test.html', {})


def redirect_test(request):
    return redirect('/redirect_test/page_one')


def page_one(request):
    return HttpResponse('Redirect :-)')
