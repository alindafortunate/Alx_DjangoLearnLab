from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

# from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from .forms import CustomUserCreationForm


# Create your views here.
def index(request):
    return render(request, "blog/home.html")


def register(request):

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login/")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "blog/register.html", context)


class ProfileManagement(UpdateView):
    pass


def profile(request):
    if request.method == "POST":
        user = User.objects.get(user=request.user)
        form = CustomUserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("/login/")
    else:
        form = CustomUserCreationForm()
    context = {"form": form}

    return render(request, "blog/profile.html", context)


def post_list(request):
    pass


class PostListView(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = "blog/post_list.html"


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.all()
    template_name = "blog/post_detail.html"


class PostCreateView(CreateView):
    model = Post
    fields = ["title", "content", "author"]
    success_url = "/posts/"
    template_name = "blog/post_form.html"


class PostUpdateView(UpdateView):
    model = Post
    fields = ["title", "content", "author"]
    success_url = "/posts/"
    template_name = "blog/post_form.html"


class PostDeleteView(DeleteView):
    model = Post
    success_url = "/posts/"
    template_name = "blog/post_confirm_delete.html"
