from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class NuevaOpinionForm(forms.Form):
    libro = forms.CharField(label='Libro', max_length=100)
    opinion = forms.CharField(label='Opinión', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user is not None and user.is_authenticated:
            self.fields['nombre'] = forms.CharField(widget=forms.HiddenInput(), initial=user.first_name)
            self.fields['apellido'] = forms.CharField(widget=forms.HiddenInput(), initial=user.last_name)
        else:
            self.fields['nombre'] = forms.CharField(label='nombre', max_length=100)
            self.fields['apellido'] = forms.CharField(label='apellido', max_length=100)




class CustomUserCreationForm(UserCreationForm):
    nombre = forms.CharField(max_length=30, required=True, help_text='Requerido.')
    apellido = forms.CharField(max_length=30, required=True, help_text='Requerido.')

    class Meta:
        model = User
        fields = ('username', 'nombre', 'apellido', 'email', 'password1', 'password2')
