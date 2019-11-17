from django import forms


class SearchForm(forms.Form):

    keyword = forms.CharField(initial="Anything", required=False)
    businesses = forms.BooleanField(initial=True, required=False)
    posts = forms.BooleanField(initial=True, required=False)
