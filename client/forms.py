from django import forms

class ScrapeForm(forms.Form):
    CHOICES = [('id', 'ID'), ('class', 'Class')]
    url = forms.URLField(label='URL')
    element_type = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    element_name = forms.CharField(label='Element Name')
