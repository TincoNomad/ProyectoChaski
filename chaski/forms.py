from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Formulario para crear usuarios 
class UserRegisterForm(UserCreationForm):

	class Meta:
		model = User
		fields = ['first_name', 'username', 'email', 'password1', 'password2']