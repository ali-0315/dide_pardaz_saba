from django import forms

from .models import Brand, Phone


class PhoneModelform(forms.ModelForm):
    class Meta:
        model = Phone
        fields = '__all__'
        exclude = ['date_added']


class BrandModelform(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
        exclude = ['date_added']
