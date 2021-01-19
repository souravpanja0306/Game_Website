from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, 'home.html')
    
def product(request):
    return render(request, 'product.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def contactus(request):
    return render(request, 'contactus.html')

def carrer(request):
    return render(request, 'career.html')

def signin(request):
    return render(request, 'signin.html')