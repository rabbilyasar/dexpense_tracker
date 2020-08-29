from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .decorators import unauthenticated_user
from django.contrib import messages
from django.shortcuts import redirect


@unauthenticated_user
def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for %s.' % username)
            return redirect('tracker:login')

    context = {'form': form}
    return render(request, 'tracker/register.html', context)


@unauthenticated_user
def loginPage(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('tracker:home')
        else:
            messages.info(request, 'Username or password incorrect')

    context = {}
    return render(request, 'tracker/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('tracker:login')
