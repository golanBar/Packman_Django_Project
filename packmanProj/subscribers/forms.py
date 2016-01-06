from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Subscriber


class DetailsMixin(forms.ModelForm): # ModelForm is used when you want a form to be based on one of your models. in this case the Subscriber model.
    class Meta:
        model = Subscriber
        fields = ('nickname', 'gender', 'age')
        # A widget is Django’s representation of an HTML input element. The widget handles the rendering of the
        # HTML, and the extraction of data from a GET/POST dictionary that corresponds to the widget.
        widgets = {
            'nickname': forms.TextInput(attrs={'class':'form-control'}),
            'gender': forms.TextInput(attrs={'class':'form-control'}),
            'age': forms.TextInput(attrs={'class':'form-control'}),
        }


class SubscriberForm(DetailsMixin, UserCreationForm):
    email = forms.EmailField(
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'})
    )
    password2 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'})
    )
