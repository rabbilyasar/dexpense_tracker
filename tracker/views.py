from django.shortcuts import redirect, render

from tracker.forms import *
# Create your views here.


def home(request):
    form = ExpenseForm()
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form_data = form.save(commit=False)
            print(form_data)
            form_data.submitted_by = request.user
            form_data.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'tracker/home.html', context)
