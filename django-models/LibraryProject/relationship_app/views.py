from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

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


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"


class LoginView(LoginView):
    template_name = "registration/login.html"


class LogoutView(LogoutView):
    template_name = "registration/logout.html"
