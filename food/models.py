from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
    name=models.CharField(max_length=100)    
    address= models.TextField()
    phone= models.CharField(max_length=15)
    
is_open=models.BooleanField(default=True)

def __str__(self):
    return self.name    



class Category(models.Model):
    name= models.CharField(max_length=100)
    description= models.CharField(blank=True)
    
def __str__(self):
    return self.name    


class FoodItem(models.Model):
    restuarant= models.ForeignKey(
    Restaurant,
    on_delete=models.CASCADE,
    related_name='food_items'
    )
    
    category= models.ForeignKey(
        Category,
    on_delete=models.CASCADE,
    related_name='category_food_items'     
    )
    
    name= models.CharField(max_length=100)
    description= models.TextField(blank=True)
    price= models.DecimalField(max_digits=10, decimal_places=2)    
    is_available= models.BooleanField(default=True)   

def __str__(self):
        return self.name               
    
    
    
class Cart(models.Model):
    user= models.OneToOneField(
        User,
on_delete=models.CASCADE,related_name='cart'    
    )    
    
created_at = models.DateTimeField(auto_now_add=True)
    
def __str__(self):
        return
        f"{self.user.username}'s Cart"
     
        
class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items'
    )

    food_item = models.ForeignKey(
        FoodItem,
        on_delete=models.CASCADE,
        related_name='cart_items'
    )

    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.food_item.name} * {self.quantity}"
    
class Order(models.Model):
    STATUS_CHOICES =[
        ('pending', 'Pending'),
        ('confirmed','Confirmed'),
        ('preparing','Preparing'),
        ('out_for_delivery','Out for Delivery'),
        ('delivered','Delivered'),
        ('cancelled','Cancelled'),
    ]
    
    
    user= models.ForeignKey(
        User,
    on_delete=models.CASCADE,
            related_name='orders'    
    )
    
    
    total_amount =models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Order#{self.id} -{self.user.username}"
    
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(
       Order,
       
on_delete=models.CASCADE,
    related_name='items'      
    ) 
    
    food_item = models.ForeignKey(
        FoodItem,
        
on_delete=models.CASCADE       
    )   
    
    
    quantity=models.PositiveIntegerField(default=1)
    
    price=models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    
    def __str__(self):
        return
        f"{self.food_item.name} *{self.quantity}"    