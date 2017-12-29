from django import forms

class SearchForm(forms.Form):
    search_key = forms.CharField(
        label='検索キー',
        max_length=20,
        required=True,
        widget=forms.TextInput(),
    )
