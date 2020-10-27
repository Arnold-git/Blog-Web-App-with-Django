from django import foms
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	email = forms.EmailFields()

	class meta:
		model = User 
		fields = ['username', 'email', 'password1', 'password2']