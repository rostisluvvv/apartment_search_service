from django.contrib import admin
from django.urls import path

from .views import index, by_rubric, ApartmentInfoCreateView


app_name = 'main_page'

urlpatterns = [

    path('', index, name='index'),
    path('add/', ApartmentInfoCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
]