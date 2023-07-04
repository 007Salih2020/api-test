from django.urls import path, include
from . import views
from django.contrib import admin

''' 
urlpatterns = [
    path('members/', views.members, name='members'),
    path('', include('members.urls')),
    path('admin/', admin.site.urls),
    path('members/details/<int:id>', views.details, name='details'),
]
'''
urlpatterns = [
    path('', views.main, name='main'),
    path('/members/', views.members, name='members'),
    path('/members/details/<int:id>', views.details, name='details'),
    path('/testing/', views.testing, name='testing'),  
    path('', include('members.urls')),
    path('admin/', admin.site.urls),
]