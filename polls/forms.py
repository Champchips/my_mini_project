from django import forms
from .models import Poll_Choice


class PollForm(forms.Form):
    picture = forms.FileField()


class ChoiceForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Poll_Choice
        fields = ['subject', 'image']
