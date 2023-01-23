from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import ApartmentInfo, Rubric


def index(request):
    aparts = ApartmentInfo.objects.all()
    rubrics = Rubric.objects.all()
    context = {'aparts': aparts,
               'rubrics': rubrics, }
    return render(request, 'main_page/index.html', context)


def by_rubric(request, rubric_id):
    aparts = ApartmentInfo.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    curent_rubric = Rubric.objects.get(pk=rubric_id)

    context = {
        'aparts': aparts,
        'rubrics': rubrics,
        'curent_rubric': curent_rubric,
    }

    return render(request, 'main_page/by_rubric.html', context)