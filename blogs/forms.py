from django import forms


class FormSearch(forms.Form):
    title = forms.CharField(max_length=45)
