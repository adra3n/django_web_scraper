from django import forms

class ScrapeForm(forms.Form):
    CHOICES = [('id', 'ID'), ('class', 'Class')]
    url = forms.URLField(label='Target URL')
    element_type = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect,label='Selector Type')
    element_name = forms.CharField(label='Element Name')
