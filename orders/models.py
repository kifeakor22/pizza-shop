from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import ModelForm

# Create your models here.
SMALL = 'small'
LARGE = 'large'
REGULAR = "Regular pizza"
SICILIAN = "Sicilian pizza"

PIZZA_SIZE_CHOICES = [(SMALL, 'S'),(LARGE, 'L'),]
PIZZA_STYLE_CHOICE = [ (REGULAR,'Regular pizza'), (SICILIAN,'Sicilian pizza')]
DINNER_SIZE_CHOICES = [(SMALL, 'small'),(LARGE, 'large'),]
SIZE_CHOICES = [(SMALL, 'small'),(LARGE, 'large'),]

class Topping(models.Model):
    topping = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=4,decimal_places=2, default=1.50)

    def __str__(self):
        return f"{self.topping} £{self.price}"

class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length= 64, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def __str__(self):
        return '{}'.format(self.name)

class Product(models.Model):
        name = models.CharField(max_length=64)
        category = models.ForeignKey(Category, on_delete=models.CASCADE)
        price = models.DecimalField(max_digits=4,decimal_places=2, default=0.0)
        stock = models.IntegerField()
        available = models.BooleanField(default=True)
        size = models.CharField(max_length=10,choices=SIZE_CHOICES,blank=True, null=True)
        pizza_style = models.CharField(max_length=20,choices=PIZZA_STYLE_CHOICE, blank=True, null=True)
        topping = models.ManyToManyField(Topping, blank=True)

        class Meta:
            ordering = ('name', )
            verbose_name = 'product'
            verbose_name_plural = 'products'

        def __str__(self):
            return f"{self.name} £{self.price}"




class PizzaForm(ModelForm):
     class Meta:
         model = Product
         fields = ['size', 'pizza_style', 'price', 'topping']
