from django.contrib import admin
from django.urls import path

from posts.views import index


urlpatterns = [
    path('main_page/', index),
    path('admin/', admin.site.urls),
]
