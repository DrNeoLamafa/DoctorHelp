import datetime
from django import forms


class RecipeForm(forms.Form):
    pillsName = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '',
            'readonly': True
        }))
    recipe = forms.CharField(
        label="Рецепт", 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Рецепт'
        }))
class DatePeople(forms.Form):
    patient = forms.CharField(
        label="ФИО пациента", 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'ФИО пациента'
        }))
    doctor = forms.CharField(
        label="ФИО врача", 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'ФИО врача'
        }))
    birthday = forms.DateField(
        widget=forms.SelectDateWidget(years=range(datetime.date.today().year - 100, datetime.date.today().year), attrs={
            'class': 'form-select',
            'style': 'width: 33%; display: inline-block;'
            }))