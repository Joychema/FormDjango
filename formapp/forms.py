
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30, label='Your Name')
    email = forms.EmailField(max_length=15, label='Your Email')
    message = forms.CharField(widget= forms.Textarea(attrs={'rows':4}), label='Your Message')