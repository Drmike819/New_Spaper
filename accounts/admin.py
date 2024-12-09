from django.contrib import admin#Se importa el módulo de administración de Django, que permite registrar modelos en el panel de administración.
from django.contrib.auth.admin import UserAdmin #Es una clase predefinida en Django que proporciona una interfaz de administración para el modelo User. Aquí la estás extendiendo para trabajar con tu modelo personalizado.

#Son formularios personalizados para crear y cambiar usuarios. 
#Esto te permite gestionar cómo se crean y editan los usuarios en el panel de administración.
from .forms import CustomUserCreationForm, CustomUserChangeForm
from . models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    #definicion de atributos de definiran que agregara uy editara los usuarios 
    add_form = CustomUserCreationForm#creacion
    form = CustomUserChangeForm#edicion
    #especifica el modela que la clase esta gestionando 
    model = CustomUser
    #Define los campos que se mostrarán en la lista de usuarios dentro del panel de administración
    list_display =[
        'email',
        'username',
        'age',
        'image',
        'is_staff',
    ]
    #Especifica los campos que se mostrarán al editar un usuario
    fieldsets = UserAdmin.fieldsets + ((None,{"fields": ('age','image',)}),)
    #Especifica los campos que se mostrarán al agregar un nuevo usuario
    add_fieldsets = UserAdmin.add_fieldsets + ((None,{'fields':('age','image',)}),)
    
 #registra el modelo al panel de django    
admin.site.register(CustomUser, CustomUserAdmin)