from django import forms
from django.forms import ModelForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product, Topping, SIZE_CHOICES, PIZZA_STYLE_CHOICE



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    address = forms.CharField(required=False, help_text='Optional.')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','address', 'password1', 'password2', ]
class PizzaForm(forms.Form):
    pizza_size = forms.CharField(max_length=3, widget=forms.Select(choices=SIZE_CHOICES),)
    pizza_style = forms.CharField(max_length=3,widget=forms.Select(choices=PIZZA_STYLE_CHOICE))
    price = forms.CharField(max_length=100)
    topping = forms.ModelMultipleChoiceField(queryset=Topping.objects.all())



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Invalid credentials, please try again.")
            if not user.is_active:
                raise forms.ValidationError("User is no longer active.")
        return super(LoginForm, self).clean(*args, **kwargs)
