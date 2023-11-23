from django.contrib import admin
from .models import Category,Product,Cart,Order
# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display=('id','name','description','image','price','category')

class AdminCart(admin.ModelAdmin):
    list_display=('id','user','product','qty','sub_total')

class AdminOrder(admin.ModelAdmin):
    list_display=('id','user','full_name','email','city','address','payment_mod','phone','order_amount','instructions','delivery_method')

admin.site.register(Category)
admin.site.register(Product,AdminProduct)    
admin.site.register(Cart,AdminCart)
admin.site.register(Order)
