from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterUserForm


# Create your views here.
def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Account created successfully, Please Login.")
            return redirect("login")
        else:
            messages.warning(request, "Error , something went wrong")
            return redirect("register")
    else:
        form = RegisterUserForm()
        context = {"form": form}
        return render(request, "account/register.html", context)


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect("place-order")
        else:
            messages.warning(request, "Something went wrong, Invalid username/password")
            return redirect("login")
    else:
        return render(request, "account/login.html")


def logout_user(request):
    logout(request)
    messages.info(request, "Session ended , successfully")
    return redirect("login")
