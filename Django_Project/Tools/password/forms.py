from django import forms
# from .views import index


class newPass(forms.Form):
    email =  forms.CharField(label="", max_length="300", widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(label="", max_length="300", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))