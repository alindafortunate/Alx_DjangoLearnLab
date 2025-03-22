from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# Create your views here.
def index(request):
    return render(request, "blog/home.html")


def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login/")
    context = {
        "form": form,
    }
    return render(request, "blog/register.html", context)


def profile(request):
    form = UserChangeForm()
    if request.method == "POST":
        form = UserChangeForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}

    return render(request, "blog/profile.html", context)


def post_list(request):
    pass
