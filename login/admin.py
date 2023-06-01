from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    is_student = forms.BooleanField(required=False)
    is_coordinator = forms.BooleanField(required=False)
    is_careercenter = forms.BooleanField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('is_student', 'is_coordinator', 'is_careercenter')

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = User
    list_display = ['username', 'email', 'is_staff', 'is_superuser', 'is_student', 'is_coordinator', 'is_careercenter']

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_student', 'is_coordinator', 'is_careercenter'),
        }),
    )

admin.site.register(User, CustomUserAdmin)
