
from django.forms import ModelForm


from .models import Humans, Auto


class Human(ModelForm):
    class Meta:
        model = Humans
        fields = '__all__'

class Auto(ModelForm):
    class Meta:
        model = Auto
        fields = '__all__'