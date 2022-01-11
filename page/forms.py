from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'w3-input w3-border', 'placeholder': 'Name'}))
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'w3-input w3-border', 'placeholder': 'Subject'}))
    message = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'w3-input w3-border', 'placeholder': 'Message'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'w3-input w3-border', 'placeholder': 'Email'}))

