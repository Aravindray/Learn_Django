from django import forms

class PostShareForm(forms.Form):
    name = forms.CharField(max_length=25)
    send = forms.EmailField()
    to = forms.EmailField()
    comment = forms.CharField(required=False, widget=forms.Textarea)
