from django import forms
from .models import registration


class registrationform(forms.ModelForm):
    class Meta:
        model = registration
        fields = ['Firstname', 'Lastname', 'Email', 'Password']
