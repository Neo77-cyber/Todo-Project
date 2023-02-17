from django.urls import path 
from todo import views


urlpatterns = [
    path('', views.allnotes, name = 'home'),
    path('del/<int:pk>', views.deletetasks, name ='del')

]