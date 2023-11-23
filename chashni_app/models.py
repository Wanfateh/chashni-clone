from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural= "categories"

    def __str__(self):
        return f'name: {self.name}'
    
class Product(models.Model):
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=500, null=True)
    image=models.ImageField(upload_to='products/')
    price=models.DecimalField(decimal_places=2,max_digits=8)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return  f'Name: {self.name}'



class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    qty=models.IntegerField(default=1)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    sub_total=models.DecimalField(decimal_places=2,max_digits=8,default=0)
    order_id = models.CharField(default=0,max_length=15)

    def __str__(self):
            return  f'Name: {self.user.username}'
    
class Order(models.Model):
     email=models.EmailField(blank=False)
     full_name=models.CharField(max_length=70,blank=False)
     phone=models.CharField(max_length=15, blank=False)
     address=models.CharField(max_length=200 ,blank=False)
     city=models.CharField(max_length=50, blank=False)
     instructions=models.CharField(max_length=255, null=True)
     payment_mod=models.CharField(max_length=100,blank=False)
     user=models.ForeignKey(User,on_delete=models.CASCADE)
     order_amount=models.DecimalField(decimal_places=2,max_digits=8,default=0)
     delivery_method=models.CharField(max_length=50, null=True)


     def __str__(self):
        return  f'Name: {self.user.username} - {self.order_amount}'