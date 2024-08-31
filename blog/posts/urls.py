
# from django.contrib import admin
from django.urls import path  
from django.conf import settings  
from django.conf.urls.static import static  
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('about1', views.about1, name='about1'),
    path('services1', views.services1, name='services1'),
    path('portfolio1', views.portfolio1, name='portfolio1'),
    path('team1', views.team1, name='team1'),
    path('blog1', views.blog1, name='blog1'),
    path('contact1', views.contact1, name='contact1'),
    path('blog-details1', views.blogdetails1, name='blog-details1')
]


if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  