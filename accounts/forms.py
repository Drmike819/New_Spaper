from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

from django import forms
# UserCreationForm:
# Sirve para manejar la creación de nuevos usuarios.
# Incluye campos como username, password1 y password2 (para verificar que las contraseñas coinciden).
# Se utiliza principalmente en vistas o formularios donde se crea un nuevo usuario, como en un formulario de registro.

# ampliar los formularios integrados UserCreationForm y UserChangeForm 
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            'username',
            'email',
            'age',
            'image',
        )

# UserChangeForm:
# Sirve para manejar la modificación de usuarios existentes.
# Permite editar campos como el nombre de usuario y otros datos de perfil, pero sin mostrar los campos de la contraseña de manera insegura.
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'age',
            'image',
        )
        
class UpdateProfileImageForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['image']  # Campo de imagen para actualizar el perfil