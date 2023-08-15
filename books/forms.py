from .models import Book
from django.forms import ModelForm, TextInput, NumberInput


class BookForm(ModelForm):

    class Meta:
        # Название модели на основе
        # которой создается форма
        model = Book
        # Включаем все поля с модели в форму
        fields = '__all__'
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
