from django.conf import settings
from django.shortcuts import redirect, render
from ACSIannuaire.mainApp.models import Tagger
from forms import LoginForm,SignupForm
from django.contrib.auth import login,logout,authenticate
from models import User

# Create your views here.
def signin_view(request):
    form = LoginForm()
    message=''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = 'Identifiants invalides.'
    return render(
        request, 'authenticator/signin.html', context={'form': form, 'message': message})

def signup_view(request):
    form =SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
        # auto-login user
        login(request, user)
        return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authenticator/signup.html', context={'form': form})

def signout_view(request):
    logout(request)
    return redirect('home')

def account(request,pk):
    products = None
    services = None
    if request.user.is_authenticated and request.user.role == 'seller':
        user = User.objects.get(id=request.user.id)
        products = user.service_set.all()
        try:
            tags = Tagger.objects.get(user=request.user)
        except:
            #products = None
            tags = None
    return render(request, 'authenticator/account.html', context={'products': products,'tags': tags})