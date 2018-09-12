from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=250)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20)
    message = forms.CharField(widget=forms.Textarea)
