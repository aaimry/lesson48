from django import forms
from store.models import CATEGORY_CHOICES


class ProductsForm(forms.Form):
    title = forms.CharField(max_length=100, required=True, label='Товар')
    description = forms.CharField(max_length=2000, required=False, label='Описание', widget=forms.Textarea())
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=True, label='Категория',
                                 initial=CATEGORY_CHOICES[0][1])
    residue = forms.IntegerField(required=True, lable='Остаток')
    price = forms.FloatField(max_lenght=7, required=True, label='Цена')
