from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('blog', views.BlogPage, name='blog'),
    path('services', views.ServicesPage, name='services'),
    path('contact', views.ContactPage, name='contact'),
    path('portfolio', views.PortfolioPage, name='portfolio'),
]