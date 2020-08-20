from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import SignUpForm


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return render (request,'app/logout.html',{username})
    else:
        form = SignUpForm()
    return render(request, 'app/register.html', {'form': form})
def func(request):
    return render(request, "app/home.html")