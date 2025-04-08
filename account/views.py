from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from .forms import CreateUserForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('store')
    else:
        form = CreateUserForm()
    
    return render(request, 'account/registration/register.html', {'form': form})
