from django.contrib import admin 
from django.urls import path 
from . import views
from .middleware import auth_middleware 


urlpatterns = [ 
	path('', views.index, name='index'), 
	path('store', views.store, name='store'), 

	path('signup', views.Signup, name='signup'), 
	path('login', views.Login, name='login'), 
	path('logout', views.logout, name='logout'), 
	path('cart', views.Order, name='order'), 
	path('check-out', views.CheckOut, name='checkout'), 
	path('orders', views.OrderView, name='ordersview'), 

] 
