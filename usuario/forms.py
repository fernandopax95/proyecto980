from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class FormularioRegistro(UserCreationForm):
    name = forms.CharField()
    lastname = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('name', 'lastname', 'email','password1','password2')

