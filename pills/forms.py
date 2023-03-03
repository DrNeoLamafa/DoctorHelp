from django import forms

class SearchForm(forms.Form):
    CHOICES = [('1', 'Поиск по имени'), ('2', 'Поиск по составу'), ('3', 'Поиск по диагнозу')] 
    searchType = forms.ChoiceField(label='', choices=CHOICES, widget = forms.Select(attrs = {'onchange' : "changeType();"}))