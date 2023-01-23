from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import ApartmentInfo


def index(request):
    aparts = ApartmentInfo.objects.order_by('-published')
    context = {'aparts': aparts}
    return render(request, 'main_page/index.html', context)
