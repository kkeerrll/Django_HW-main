from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserCreationForm, EmailVerificationForm, PasswordResetForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            return redirect('email_verification')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def email_verification(request):
    if request.method == 'POST':
        form = EmailVerificationForm(request.POST)
        if form.is_valid():
            # Ваш код отправки письма с верификацией почты
            return redirect('login')
    else:
        form = EmailVerificationForm()
    return render(request, 'email_verification.html', {'form': form})

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'login.html')

def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            # Ваш код восстановления пароля пользователя
            return redirect('password_reset_done')
    else:
        form = PasswordResetForm()
    return render(request, 'password_reset.html', {'form': form})
