from django import forms
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your username'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'your password'}))


class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your email'}))
    password1 = forms.CharField(label='password', max_length=50,
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control', 'placeholder': 'your password'}))
    password2 = forms.CharField(label='confirm password', max_length=50,
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control', 'placeholder': 'your password'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email)
        if user.exists():
            raise forms.ValidationError('email vojod darad')
        return email

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password1')
        p2 = cleaned_data.get('password2')

        if p1 and p2:
            if p1 != p2:
                raise forms.ValidationError('password must match')
