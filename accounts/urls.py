from django.urls import path
from .views import SignUpView, user_logout, update_profile_image

#urls del salir e inicio de sesion tambien de actualizar foto de perfil
urlpatterns =[
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', user_logout, name='logout'),
    path('update_profile_image/', update_profile_image, name='update_profile_image'),
]