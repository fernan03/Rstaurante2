from ast import pattern
from turtle import textinput
from django import forms

class FormularioEmpleados(forms.Form):

    CARGO=(
        (1,'Chef'),
        (2,'Administrador'),
        (3,'Mesero'),
        (4,'Ayudante')
    )

    nombre=forms.CharField(
        required=True,
        max_length=5,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    apellido=forms.CharField(
        required=True,
        max_length=20,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    fotografia=forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    tipo=forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={'class':'form-control mb-5'}),
        choices=CARGO
    )
    salario=forms.CharField(
         required=True,
        max_length=20,
        widget=forms.NumberInput(attrs={'class':'form-control mb-5'})
    )
    contacto=forms.CharField(
         required=True,
        max_length=20,
        widget=forms.NumberInput(attrs={'class':'form-control mb-5'})
    )