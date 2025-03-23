from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "author"]


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Enter Email")

    class Meta(UserCreationForm.Meta):

        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):

        user = User.objects.create_user(
            self.cleaned_data["username"],
            self.cleaned_data["email"],
            self.cleaned_data["password1"],
        )

        return user
