from django import forms
from django.contrib.auth.models import User

class DweetsForm(forms.Form):

    tweet_text = forms.CharField(widget=forms.Textarea)