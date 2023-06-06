from django import forms
# from .views import index


class newTask(forms.Form):
    body = forms.CharField(label = "",max_length="300",widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task'}))

    