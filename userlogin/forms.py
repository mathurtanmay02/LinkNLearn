from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import authorization

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['username'].help_text = None

class AuthorizationForm(forms.ModelForm):
    class Meta:
        model = authorization
        fields = ["name", "position", "company_name" ,"email"]
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'position' : forms.TextInput(attrs={'class' : 'form-control'}),
            'company_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
        }

        def __init__(self, *args, **kwargs):
            super(AuthorizationForm, self).__init__(*args, **kwargs)
            self.fields['name'].widget.attrs['class'] = 'form-control'
            self.fields['position'].widget.attrs['class'] = 'form-control'
            self.fields['company_name'].widget.attrs['class'] = 'form-control'
            self.fields['email'].widget.attrs['class'] = 'form-control'

            self.fields['name'].help_text = None
            self.fields['position'].help_text = None
            self.fields['company_name'].help_text = None
            self.fields['email'].help_text = None

