from django import forms


class Submit(forms.Form):
    category = forms.CharField(required=True, label='Submit A Category')
    candidate = forms.CharField(required=True, label='Submit Your Candidate')
