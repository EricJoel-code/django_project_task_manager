from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Vista de registro de usuario
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserRegistrationForm()
            
    return render(request, 'register.html', {'form': form})

# vista de login (Usando la vista incorporada de Django)
class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = AuthenticationForm
    
    def get_success_url(self):
        return '/myapp/home/'
    
    def form_invalid(self, form):
        # Si la autenticación falla, renderiza el formulario con un mensaje de error
        return render (self.request, self.template_name, {
            'form': form,
            'error_message': 'Invalid username or password.'
        })
    
# Vista de cierre de sesión
@login_required
def singout(request):
    logout(request)
    return redirect('login')
    
# Vista para gestionar el perfil de usuario
@login_required
def profile(request):
    return render(request, 'profile.html')