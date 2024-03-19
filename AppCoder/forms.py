from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppCoder.models import Avatar

class ViajeFormulario(forms.Form):
    nombre = forms.CharField()
    duracion = forms.IntegerField()
    
class LibroFormulario(forms.Form):
    nombre = forms.CharField()
    autor = forms.CharField()
    
class Actividad_FisicaFormulario(forms.Form):
    nombre = forms.CharField()
    frecuencia = forms.IntegerField()
    
class CursoFormulario(forms.Form):
    nombre = forms.CharField()
    docente = forms.CharField()

class UsuarioRegistro(UserCreationForm):
    
    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)    
    password2 = forms.CharField(label = "Repetir la contraseña", widget=forms.PasswordInput)
    
    class Meta:
        
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]
    
class FormularioEditar(UserCreationForm):
    
    class Meta:
        
        model = User
        fields = ["email", "first_name", "last_name", "password1", "password2"]

class AvatarFormulario(forms.ModelForm):
    
    class Meta:
        
        model = Avatar
        fields = ["imagen"]