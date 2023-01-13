from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from . models import Category, Product, Topping
from . forms import SignUpForm, LoginForm, PizzaForm
from django.contrib.auth.decorators import login_required
from django.conf import settings


from django.contrib.auth.models import User

# Create your views here.

def index(request):

    context = {
     "menu": Topping.objects.all()
    }
    return render(request,"orders/index.html", context)
def home_view(request):
    return render(request, 'home.html')
def signup_view(request):
    form = SignUpForm(request.POST)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = SignUpForm()
    return render(request, 'orders/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

def login_view(request):
    form= LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('signup')
    return render(request,"orders/login.html", {'form':form})
@login_required(login_url='login')
def home(request, method="POST"):
    sub = Category.objects.get(id=1)
    salad = Category.objects.get(id=3)
    pasta = Category.objects.get(id=2)
    dinner = Category.objects.get(id=4)
    pizza = Category.objects.get(id=5)
    if request.method =="POST":
        sub_id= request.POST.get('drop1', False)
        print(sub_id)

    user = request.user
    context = {
    "key": settings.STRIPE_PUBLIC_KEY,
    "user": user,
    "subs": Product.objects.filter(category=sub),
    "pastas": Product.objects.filter(category=pasta),
    "salads": Product.objects.filter(category=salad),
    "dinners":Product.objects.filter(category=dinner),
    'pizza': Product.objects.filter(category=pizza),
    }
    return render(request, "orders/home.html", context)

@login_required(login_url='login')
def order(request, method="POST"):
     if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PizzaForm(request.POST)
        if form.is_valid():
            pizza_size = form.cleaned_data['pizza_size']
            pizza_style = form.cleaned_data['pizza_style']
            topping = form.cleaned_data['topping']
            price = 23
            return HttpResponse(price)
        # check whether it's valid:
        #we'll create a blank form
     else:
         form = PizzaForm()
         return render(request,"orders/register.html",{'form':form})


@login_required
def add_to_cart(request,pro_id):
    order = get_object_or_404(Book, pk=book_id)
    cart,created = Cart.objects.get_or_create(user=request.user, active=True)
    cart.add_to_cart(book_id)
    return redirect('cart')
