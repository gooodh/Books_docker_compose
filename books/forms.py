from .models import Book
from django.forms import ModelForm, TextInput, NumberInput


class WorkForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'cover']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название',
                }),
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автор',
                }),
            'price': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Стоимость',
                }),
        }
