from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Category, Smartphones
from django.core.exceptions import ValidationError

class AddPostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'


    class Meta():
        model = Smartphones
        fields = ['post_title', 'post_content', 'slug', 'cat']
        widgets = {
            'post_content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }

    def clean_post_title(self):
        title = self.cleaned_data['post_title']
        if len(title)>200:
            raise ValidationError('Длина заголовка слишком большая')

class UserRegister(UserCreationForm):
    username = forms.CharField(label='Имя', widget=forms.TextInput())
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput())

