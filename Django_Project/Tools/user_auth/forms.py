from django import forms
# from .views import index
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class user_form(forms.Form):
    username =  forms.CharField(label="", max_length="300", widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder': 'Username'}))
    password = forms.CharField(label="", max_length="300", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))
    
class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email', 'password1','password2')
  
    def __init__(self,*args,**kwargs):
        super(RegisterUserForm, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'