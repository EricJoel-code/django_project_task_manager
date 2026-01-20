from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

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