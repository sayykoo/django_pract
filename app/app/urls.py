"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main_app.views import about_us, shop, posts, items_shop_detail, register,search_items, login_user, profile_view, cart_detail
from main_app import views
from django.conf import settings
from django.conf.urls.static import static
from main_app.views import create_order

# get_info, get_students, 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', posts, name='home'),
    path('about-us/', about_us, name='about'),
    path('shop/', shop, name='shop'),
    path('search/', search_items, name='search'),
    path('shop/<int:pk>', items_shop_detail, name='shop_detail'),
    path('register_page/', register, name='register'),
    path('login_page/', login_user, name='login'),
    path('profile/', profile_view, name='profile'),
    path('cart/', cart_detail, name='cart'),
    path('order/', create_order, name='create_order'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
