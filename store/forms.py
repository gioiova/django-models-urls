from django import forms
from store.models import Product
# class ProductForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     description = forms.CharField(widget=forms.Textarea)
#     price = forms.DecimalField(max_digits=10, decimal_places=2)
#     stock = forms.IntegerField(min_value=0)
#     is_sale = forms.BooleanField(required=False)
#     category = forms.ChoiceField(choices=[])  # Choices will be populated dynamically


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        #fields = '__all__'
        exclude = ['is_sale']
    