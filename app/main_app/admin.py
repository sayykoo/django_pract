from django.contrib import admin
from .models import Authors, ShopModel, Posts, Order, OrderItem
# Student, Course, Teacher, MyModel, 
# Register your models here.

@admin.register(Authors, ShopModel, Posts)
class AdminAuthor(admin.ModelAdmin):
    pass

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_user', 'customer_user', 'order_date', 'status')
    search_fields = ('customer_user', 'customer_user', 'status')
    list_filter = ('status', 'order_date')
    inlines = [OrderItemInline]
                     
