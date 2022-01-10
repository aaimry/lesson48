from django import forms
from store.models import CATEGORY_CHOICES


class ProductsForm(forms.Form):
    title = forms.CharField(max_length=100, required=True, label='Товар')
    description = forms.CharField(max_length=2000, required=False, label='Описание', widget=forms.Textarea())
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=True, label='Категория',
                                 initial=CATEGORY_CHOICES[0][1])
    residue = forms.IntegerField(min_value=0, required=True, label='Остаток')
    price = forms.DecimalField(max_digits=9, decimal_places=2, required=True, label='Цена')
