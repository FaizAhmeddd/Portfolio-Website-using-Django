from django.contrib import admin
from django.urls import path , include
from home import views  

admin.site.site_header = "Login to Admin Dashboard"
admin.site.site_title = "Welcome to Portfolio Website"
admin.site.index_title = "Welcome to the portal"



urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('projects',views.projects,name='projects'),
    path('contact',views.contact,name='contact')
]
