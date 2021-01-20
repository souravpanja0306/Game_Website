from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('product', views.product, name='product'),
    path('about', views.about, name='about'),
    path('service', views.service, name='service'),
    path('contactus', views.contactus, name='contactus'),
    path('career', views.career, name='career'),
    path('signin', views.signin, name='signin'),
    path('login', views.login, name='login'),
    path('forgetpass', views.forgetpass, name='forgetpass'),
]