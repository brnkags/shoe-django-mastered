from django import forms
from djangoshoeapp.models import Shoes


class ShoesAppForm(forms.ModelForm):
    class Meta:
        model = Shoes
        fields = '__all__'
