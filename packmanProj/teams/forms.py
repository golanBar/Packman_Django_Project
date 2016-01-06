from django import forms

from .models import Team


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('name', 'desc',)
        widgets = {
            'name': forms.TextInput(
                    attrs={
                        'placeholder': 'Set the team\'s name',
                        'class': 'col-md-12 form-control'   # widget Class is a css class to make the form look better
                    }
            ),
            'desc': forms.TextInput(
                    attrs={
                        'placeholder': 'Enter a short description',
                        'class':'form-control'
                    }
            ),
        }
