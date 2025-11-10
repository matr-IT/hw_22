from django import forms
from .models import Blogs

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ['title', 'body', 'photo', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Введите содержание'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'is_published': forms.RadioSelect(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'is_published': 'Статус публикации',
        }

