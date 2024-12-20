
from django.contrib import admin
from django.urls import path,include
from .import views 
urlpatterns = [
    path('',views.index,name="store"),
    path('about',views.about,name="about"),
    path('blog',views.blog,name="blog"),
    path('contact',views.contact,name="contact"),
    path('detail',views.detail,name="detail"),
    path('feature',views.feature,name="feature"),
    path('product',views.product,name="product"),
    path('service',views.service,name="service"),
    path('team',views.team,name="team"),
    path('testimonial',views.testimonial,name="testimonial"),
    
     
]
