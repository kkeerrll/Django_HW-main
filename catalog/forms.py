from django import forms
from django.shortcuts import render

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in forbidden_words:
            if word.lower() in name.lower():
                raise forms.ValidationError("Нельзя использовать запрещенные слова в названии продукта.")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in forbidden_words:
            if word.lower() in description.lower():
                raise forms.ValidationError("Нельзя использовать запрещенные слова в описании продукта.")
        return description

# Пример использования формы
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            # дополнительные действия, если форма валидна
            # например, редирект на страницу с деталями продукта
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Product, Version

class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ['product', 'version_number', 'version_name', 'is_active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))

def create_version(request):
    if request.method == 'POST':
        form = VersionForm(request.POST)
        if form.is_valid():
            form.save()
            # дополнительные действия, если форма валидна
            # например, редирект на страницу с деталями продукта
    else:
        form = VersionForm()
    return render(request, 'create_version.html', {'form': form})

