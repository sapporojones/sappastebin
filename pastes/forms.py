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

    paste_body = forms.CharField(strip=False, widget=forms.Textarea(attrs={'rows': 50, 'cols': 175}))
    # encryption_key = forms.CharField(required=False)
    # password_protect = forms.BooleanField(required=False)

    class Meta:
        model = Pastes
        # exclude = ['date_created',]
