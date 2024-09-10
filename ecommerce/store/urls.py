from django.contrib import admin 
from django.urls import path 
from . import views


urlpatterns = [ 
	path('', views.index.as_view(), name='index'), 
	path('store', views.store, name='store'), 

	path('signup', views.Signup.as_view(), name='signup'), 
	path('login', views.Login.as_view(), name='login'), 
	path('logout', views.logout, name='logout'), 
	path('cart', views.Cart, name='cart'), 
	path('check-out', views.CheckOut.as_view(), name='checkout'), 
	path('orders', views.OrderView.as_view(), name='ordersview'), 

] 
