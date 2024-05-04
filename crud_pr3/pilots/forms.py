from django.forms import ModelForm
from .models import Pilots


class ProductForm(ModelForm):
    class Meta:
        model = Pilots
        fields = '__all__'