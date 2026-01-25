from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "input", "placeholder": ""})
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "input", "placeholder": ""})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "input", "placeholder": ""})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "input", "placeholder": ""})
    )
    password1 = forms.CharField( required=True,
        widget=forms.PasswordInput(attrs={"class": "input", "placeholder": ""})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "input", "placeholder": ""})
    )

    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está en uso.")
        return email