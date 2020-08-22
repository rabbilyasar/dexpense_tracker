from django.shortcuts import redirect, render
from django.db.models import Q

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required

from .forms import *
from .filters import ExpenseFilter
from .decorators import unauthenticated_user, allowed_users, restrict_auditor


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


@login_required(login_url='tracker:login')
@restrict_auditor
def home(request):
    # all expenses
    expenses = Expense.objects.filter(
        status="pending").order_by('-date_created')
    myFilter = ExpenseFilter(request.GET, queryset=expenses)
    expenses = myFilter.qs
    # all expenses pagination
    paginator = Paginator(expenses, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # rejected expenses
    rejected_expenses = Expense.objects.filter(status='rejected')
    # all expenses pagination
    paginator = Paginator(rejected_expenses, 5)
    page_number = request.GET.get('page')
    rejected_expenses_page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj, 'myFilter': myFilter,
               'rejected_expenses_page_obj': rejected_expenses_page_obj}
    return render(request, 'tracker/home.html', context)


@login_required(login_url='tracker:login')
def approvedExpenses(request):
    approved_expenses = Expense.objects.filter(status='approved')
    myFilter = ExpenseFilter(request.GET, queryset=approved_expenses)
    expenses = myFilter.qs

    paginator = Paginator(expenses, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj, 'myFilter': myFilter}
    return render(request, 'tracker/approved_expenses.html', context)


@login_required(login_url='tracker:login')
@allowed_users(['manager', 'employee'])
def createExpense(request):
    form = ExpenseForm()
    if request.method == 'POST':
        form = ExpenseForm(request.POST, request.FILES)
        if form.is_valid():
            form_data = form.save(commit=False)
            print("image:", form_data.image)
            form_data.submitted_by = request.user
            form_data.save()
            messages.success(request, 'Data created successfully')
            return redirect('tracker:home')
    context = {'form': form}
    return render(request, 'tracker/expense_form.html', context)


@login_required(login_url='tracker:login')
@allowed_users(['manager', 'employee'])
def updateExpense(request, pk):
    expense = Expense.objects.get(id=pk)
    form = ExpenseForm(instance=expense)

    if request.method == 'POST':
        form = ExpenseForm(request.POST, request.FILES, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data updated successfully')
            return redirect('/')
    context = {'form': form}
    return render(request, 'tracker/expense_form.html', context)


@login_required(login_url='tracker:login')
@allowed_users(['manager', 'employee'])
def deleteExpense(request, pk):
    expense = Expense.objects.get(id=pk)

    if request.method == "POST":
        expense.delete()
        messages.success(request, 'Data deleted successfully')
        return redirect('/')

    context = {'item': expense}
    return render(request, 'tracker/delete.html', context)


@login_required(login_url='tracker:login')
@allowed_users(['manager'])
def changeStatus(request, pk):
    expense = Expense.objects.get(id=pk)
    if request.method == 'POST':
        status = request.POST.get("status")
        Expense.objects.filter(id=pk).update(status=status)

        messages.success(request, 'Status changed successfully')
        return redirect('tracker:home')
    context = {'expense': expense}
    return render(request, 'tracker/change_status.html', context)
