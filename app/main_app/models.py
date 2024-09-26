from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.test import TestCase
from .forms import RegisterForm
from django.urls import reverse
    
class Authors(models.Model):
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    images = models.ImageField(upload_to='images/')
    
class ShopModel(models.Model):
    title = models.CharField(max_length=100, null=True)
    price = models.CharField(max_length=10, null=True)
    image = models.ImageField(upload_to='images/shop/')

class MyModel(models.Model):
    title = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='images/')

class Posts(models.Model):
    title = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    date = models.DateField()
    image = models.ImageField(upload_to='images/posts/')
    
class PaymentStatus(models.TextChoices):
    PENDING = 'На рассмотрении'
    PROCESSED = 'В обработке'
    SHIPPED = 'Отправлен'
    DELIVERED = 'Доставлен'
    
class Order(models.Model):
    customer_user = models.ForeignKey(User, on_delete = models.CASCADE)
    customer_email = models.EmailField()
    order_date = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length=50, choices=PaymentStatus)
    paid = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Order {self.id} for {self.customer_user.username}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete = models.CASCADE)
    subject = models.ForeignKey(ShopModel, on_delete = models.CASCADE)
    quantity = models.IntegerField()
    
    def __str__(self):
        return f'{self.quantity} of {self.subject} for {self.order}'
    
class OrderForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = ['customer_email']
        

    
    
    