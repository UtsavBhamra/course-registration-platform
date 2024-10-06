from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm,StudentCreateForm
from .models import Student,Faculty

def register(request):
    if request.method=='POST':
        form = CustomUserCreationForm(request.POST)
        print(form.user_type)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request,'accounts/register.html',{"form":form})
    
def login_view(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
    return render(request, 'accounts/login.html')
    
def logout_view(request):
    logout(request)
    return redirect('login')

