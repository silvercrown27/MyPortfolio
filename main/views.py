from django.shortcuts import render


# Create your views here.

def HomePage(request):
    return render(request, 'index.html')


def BlogPage(request):
    return render(request, 'blog.html')


def ContactPage(request):
    return render(request, 'contact.html')


def ServicesPage(request):
    return render(request, 'services.html')


def PortfolioPage(request):
    return render(request, 'portfolio.html')
