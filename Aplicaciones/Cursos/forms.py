from django import forms
from django.contrib.auth.models import User

class RegistroUsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirmar Contraseña')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return cleaned_data
