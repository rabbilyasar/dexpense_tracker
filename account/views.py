from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect

from .decorators import unauthenticated_user
from .forms import LoginForm, RegisterForm


@unauthenticated_user
def registerPage(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for %s.' % username)
            return redirect('account:login')

    context = {'form': form}
    return render(request, 'account/register.html', context)


@unauthenticated_user
def loginPage(request):
    form = LoginForm()
    context = {'form': form}

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('tracker:home')
        else:
            messages.info(request, 'Username or password incorrect')

    context = {}
    return render(request, 'account/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('account:login')
