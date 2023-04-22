from django import forms

class NuevaOpinionForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    apellido = forms.CharField(label='Apellido', max_length=100)
    libro = forms.CharField(label='Libro', max_length=100)
    opinion = forms.CharField(label='Opinión', widget=forms.Textarea)