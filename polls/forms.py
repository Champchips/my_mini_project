from django import forms
class PollForm(forms.Form):
    picture = forms.FileField()