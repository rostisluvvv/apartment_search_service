from django.forms import ModelForm

from .models import ApartmentInfo


class ApartmentInfoForm(ModelForm):

    class Meta:
        model = ApartmentInfo
        fields = ('title', 'content', 'photo', 'address', 'apartment_area', 'price', 'contact', 'rubric')