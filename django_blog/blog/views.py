from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post


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
    template_name = "blog/post_create.html"


class PostUpdateView(UpdateView):
    model = Post
    template_name = "blog/post_update.html"


class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
