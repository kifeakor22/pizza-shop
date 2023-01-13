from django.contrib import admin

# Register your models here.
from . models import Category,Product,Topping
from cart.models import Cart, CartItem


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields ={'slug':('name',)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price','size','pizza_style','category', 'stock', 'available']
    list_editable =['price','stock','available']
    list_per_page = 20
admin.site.register(Product,ProductAdmin,)
admin.site.register(Topping)
admin.site.register(Category,CategoryAdmin,)
admin.site.register(Cart)
admin.site.register(CartItem)
