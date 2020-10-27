from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'description', 'price']

class ProductFilterForm(forms.Form):
    name = forms.CharField(label='Name:', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Description:', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    price_min = forms.DecimalField(label='Min price:', required=False, min_value=0, max_digits=9, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    price_max = forms.DecimalField(label='Max price:', required=False, min_value=0, max_digits=9, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    category = forms.ModelChoiceField(label='Category:', required=False, queryset=Category.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    # category = forms.ModelMultipleChoiceField(label='Category:', required=False, queryset=Category.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'form-control'}))

class ImportCategoriesForm(forms.Form):
    file = forms.FileField()

    def import_csv(self, file):
        try:
            file_ = file.open(mode='r')
            for category in file_.readlines():
                cat = category.decode('utf-8').replace('\n', '')
                Category.objects.create(name=cat)
            return True
        except:
            return False
