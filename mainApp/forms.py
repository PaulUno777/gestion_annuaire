from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput,EmailInput,DateInput,PasswordInput,Form,CharField


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name','birthday')
        widgets = {
            'username': TextInput(attrs={'class':'input','minlength':'5'}),
            'email': EmailInput(attrs={'class':'input'}),
            'first_name': TextInput(attrs={'class':'input'}),
            'last_name': TextInput(attrs={'class':'input'}),
            'birthday': DateInput(attrs={'class':'input','type':'date'}),
        }

class LoginForm(Form):
    username = CharField(max_length=63,widget=TextInput(attrs={'class':'input'}) ,label='Nom d’utilisateur')
    password = CharField(max_length=63, widget=PasswordInput(attrs={'class':'input','type':'password'}), label='Mot de passe')