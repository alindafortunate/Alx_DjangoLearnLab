from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Author, Book, Library, Librarian, UserProfile
from .models import CustomUser


# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "is_staff", "is_superuser")


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
admin.site.register(UserProfile)
