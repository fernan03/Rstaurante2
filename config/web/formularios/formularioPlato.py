from ast import pattern
from turtle import textinput
from django import forms

class FormularioPlatos(forms.Form):

    PLATOS=(
        (1,'Entrada'),
        (2,'Platos Fuerte'),
        (3,'Postre')
    )

    nombre=forms.CharField(
        required=True,
        max_length=19,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    descripcion=forms.CharField(
        required=True,
        max_length=200,
        widget=forms.Textarea(attrs={'class':'form-control mb-3'})
    )
    fotografia=forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    precio=forms.CharField(
         required=True,
        max_length=20,
        widget=forms.NumberInput(attrs={'class':'form-control mb-5'})
    )
    tipo=forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={'class':'form-control mb-5'}),
        choices=PLATOS
    )