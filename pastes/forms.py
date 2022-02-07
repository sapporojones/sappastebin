from django import forms
from .models import Pastes
from django.forms import ModelForm


class PastesForm(forms.Form):
    # def __init__(self, *args, **kwargs):
    #     super(PastesForm, self).__init__(*args, **kwargs)
    #     self.fields['paste_body'].strip = False
    #
    # class Meta:
    #     model = Pastes
    #     fields = "__all__"

    paste_body = forms.CharField(strip=False, widget=forms.Textarea(attrs={'rows': 30, 'cols': 155, 'style': 'width: 95%; height: 75%; align: center'}))
    encryption_key = forms.CharField(required=False)
    password_protect = forms.BooleanField(required=False)

    class Meta:
        model = Pastes
        # exclude = ['date_created',]


class PasswordEntry(forms.Form):
    user_password = forms.CharField(required=True)

    class Meta:
        model = Pastes
