from django import forms
from django.contrib.auth.models import User
from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput, BootstrapUneditableInput

class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label="username",
        error_messages={'required': 'please enter username'},
        widget=forms.TextInput(
            attrs={
                'placeholder':"username",
            }
        ),
    )    
    password = forms.CharField(
        required=True,
        label="password",
        error_messages={'required': 'please enter password'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':"password",
            }
        ),
    )  
    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError("username and password is not null")
        else:
            cleaned_data = super(LoginForm, self).clean()
