from django.urls import path 
from todo import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('del/<int:pk>', views.deletetask, name ='deletetask'),
    path('edittask/<int:pk>', views.edittask, name = 'edittask')

]