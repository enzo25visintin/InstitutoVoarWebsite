from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserForm

# Create your views here.


def home(request):
    return render(request, 'ivw/home.html')

def about(request):
    return render(request, 'ivw/about.html')

def user_list(request):
    users = User.objects.all()
    return render(request, 'ivw/user_list.html', {'users': users})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'ivw/user_form.html', {'form': form})

def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'ivw/user_form.html', {'form': form})



