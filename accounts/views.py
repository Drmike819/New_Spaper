from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages  # Para mostrar mensajes de error o éxito

from .forms import UpdateProfileImageForm

# Create your views here.

#vista para poder registarse
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    # Incluir request.FILES para manejar archivos de imagen
    def form_valid(self, form):
        # Asignar la imagen subida al formulario
        form.instance.image = self.request.FILES.get('image')
        # Llamar a la implementación del método padre para devolver la respuesta
        return super().form_valid(form)
 
#vista para cerrar sesion      
@login_required
def user_logout(request):
    logout(request)
    return render(request, 'registration/logout.html')



@login_required
def update_profile_image(request):
    # obtiene a el usuario que esta logeado
    user = request.user
    # verifica el metodo de pregunta
    if request.method == 'POST':
        # llama al formulario para que lo  muestre en pantalla
        form = UpdateProfileImageForm(request.POST, request.FILES, instance=user)
        # s el formulario se ejecuto de forma correcta 
        if form.is_valid():
            # se guarda la imagen subida
            form.save()
            messages.success(request, "¡Imagen de perfil actualizada con éxito!")
            return redirect('home')  # Redirige a la página de inicio o la que prefieras
        # si hay un error en el formulario se mustra un mensaje de error en consola
        else:
            messages.error(request, "Hubo un error al actualizar tu imagen de perfil. Por favor, intenta nuevamente.")
            print(form.errors)  # Esto imprime los errores en la consola para depuración
    else:
        form = UpdateProfileImageForm(instance=user)  # Instancia del usuario autenticado
    # nos retorna a la vista de actualizacion de foto de perfil
    return render(request, 'update_profile_image.html', {'form': form})
