from django.forms import ModelForm, Textarea
from .models import *



class PurchaseForm(ModelForm):
    class Meta:
        model = ShoeCart
        fields = ['color_selected_id', 'size_selected_id', 'purchased_quantity']  