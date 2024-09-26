from django.shortcuts import render, redirect
from django.db.models import Q
from django.urls import reverse
from django.contrib.auth import login, authenticate
from .forms import RegisterForm, LoginForm
from django.http import HttpRequest
from .models import MyModel, Authors, ShopModel, Posts, OrderForm, OrderItem
from django.contrib.auth.decorators import login_required
from .profile import Profile
from .cart import CartSession
from django.test import TestCase
from django.contrib.auth.models import User


    
def about_us(request):
    authors = Authors.objects.all()
    return render(request, 'about.html', context={
        'authors': authors,
    })
    
def shop(request):
    shop_item = ShopModel.objects.all()
    return render(request, 'shop.html', context={
        'shop_item': shop_item,
    })

def items_shop_detail(request, pk):
    item = ShopModel.objects.get(pk=pk)
    return render(request, 'shop_detail.html', context={
        'item': item,
    })
    
def posts(request):
    posts = Posts.objects.all()
    return render(request, 'home.html', context={
        'title': 'Главная',
        'posts': posts,
    })
    
def search_items(request):
    if request.method == 'GET':
        search = request.GET['search']
        print(search)
        
        items = ShopModel.objects.filter(
            Q(title__icontains = search)
        )
        print(items)
        return render(request, template_name='shop.html', context={
            'shop_item': items,
        })
    return (redirect(reverse('home')))


def register(request: HttpRequest):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('register')
    else:
        form = RegisterForm()
    return render(request, 'register.html', context={
            'title': 'Регистрация',
            'form': form,
        })
    
def login_user(request: HttpRequest):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', context={
        'title': 'Авторизация',
        'form': form,
        })
    
@login_required(login_url = 'login')    
def profile_view(request: HttpRequest):
    user = Profile.objects.select_related('user').get(user = request.user)
    return render(request, 'user_profile.html', context={
        'user': user,
        'title': "Профиль"
    })
    
    
def cart_add(request: HttpRequest, itemkitch_id):
    cart = CartSession(request.session)
    itemkitch = get_object_or_404(ShopModel, id = itemkitch_id)
    cart.add(itemkitch = itemkitch)
    
    return redirect(reverse('cart_detail'))

def cart_remove(request: HttpRequest, itemkitch_id):
    cart = CartSession(request.session)
    itemkitch = get_object_or_404(ShopModel, id = itemkitch_id)
    cart.remove(itemkitch = itemkitch)
    
    return redirect(reverse('cart_detail'))

def cart_detail(request: HttpRequest):
    cart = CartSession(request.session)
    return render(request, 'cart_detail.html', context={
        'cart': cart
    })
    
@login_required(login_url='login')
def create_order(request: HttpRequest):
    cart = CartSession(request.session)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit = False)
            order.customer_user = request.user
            order.save()
            for item_cart in cart:
                OrderItem.objects.create(order = order, subject = item_cart['subject'], quantity = item_cart['quantity']).save()
            cart.clear()
            return redirect(reverse('profile'))
    else:
        form = OrderForm()
        