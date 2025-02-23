from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test

from django.contrib import messages


from .models import Book
from .models import Library


# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {"books": books}

    return render(request, "relationship_app/list_books.html", context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"


def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Your account has been created, you can login.")
            return redirect("/relationship_app/login")
    else:
        form = UserCreationForm()
    context = {"form": form}
    return render(request, "relationship_app/register.html", context)


def LoginView(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, "registration/register.html")
    else:
        return render(request, "details not matching")


def LogoutView(request):
    logout(request)
    return render(request, "registration/logout.html")


def is_admin(user):
    user.userprofile.role == "Admin"


def is_librarian(user):
    user.userprofile.role == "Librarian"


def is_member(user):
    user.userprofile.role == "Member"


@user_passes_test(is_admin, login_url="/relationship/login")
def admin_view(request):
    return HttpResponse("relationship_app/admin_view.html")


@user_passes_test(is_librarian, login_url="/relationship/login")
def librarian_view(request):
    return HttpResponse("relationship_app/librarian_view.html")


@user_passes_test(is_member, login_url="/relationship/login")
def member_view(request):
    return HttpResponse("relationship_app/member_view.html")


# Authentication views.
