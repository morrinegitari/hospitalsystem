
from django.contrib import admin
from django.urls import path
from Hospitalapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('starter/', views.starter,name='starter'),
    path('about/', views.about,name='about'),
    path('service/', views.about,name='service'),
    path('appointment/', views.appointment,name='appointment'),
    path('department/', views.department,name='department'),
    path('doctors/', views.doctors,name='doctors'),
    path('contact/', views.contact,name='contact'),
]
