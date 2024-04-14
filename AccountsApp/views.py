from django.shortcuts import render, redirect
from .forms import CreateSignUpForm,CreateLogInForm
from .models import RoleModel
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout

def ViewSignUp(request):
    form = CreateSignUpForm()
    if request.method == 'POST':
        form = CreateSignUpForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Você foi inscrito com sucesso.')
            return redirect('AccountsApp:LogInView')
        else:
            messages.error(request, form.errors)
    context = {'form':form}
    return render(request, 'AccountsApp/SignUp.html', context)

def ViewLogIn(request):
    form = CreateLogInForm()
    Roles = RoleModel.objects.all()
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('Role')
        user = authenticate(request, email=email, password=password, role=role)
        if user is not None:
            login(request, user)
            messages.success(request, 'Você foi logado com sucesso.')
            return redirect('HomeApp:HomePageView')
        else:
            messages.error(request, 'credenciais de login inválidas')
            context = {'form': form, 'Roles': Roles}
            return render(request, 'AccountsApp/LogIn.html', context)
    else:
        context = {'form': form, 'Roles': Roles}
        return render(request, 'AccountsApp/LogIn.html', context)
    
def ViewLogOut(request):
    logout(request)
    return redirect('AccountsApp:LogInView')