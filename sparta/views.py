import re
from django.http import HttpResponse
from django.shortcuts import render


def test(request):
    return HttpResponse('Hello, World!')


def template_test(request):
    return render(request, 'test.html')