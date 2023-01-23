from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path('main_page/', include('main_page.urls')),
    path('admin/', admin.site.urls),
]
