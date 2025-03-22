from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# Create your views here.
def register(request):
    form = UserCreationForm
    if request.method == "POST":
        if form.is_valid():
            form.save()
    return render(request, "blog/register.html")


def profile(request):
    form = UserChangeForm
    if request.method == "POST":
        if form.is_valid():
            form.save()

    return render(request, "blog/profile.html")
