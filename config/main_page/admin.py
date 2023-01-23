from django.contrib import admin

from .models import ApartmentInfo, Rubric


class ApartmentInfoAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'content', 'address', 'apartment_area', 'price', 'published', 'rubric')
    search_fields = ('title', 'content')
    list_filter = ('published',)
    empty_value_display = '-пусто-'


admin.site.register(ApartmentInfo, ApartmentInfoAdmin)
admin.site.register(Rubric)