from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView,  UpdateView, DetailView, DeleteView
from .models import Task
from .forms import TodoForm
from urllib import request
from django.urls import reverse_lazy

# Create your views here.





def allnotes(request, ):

     notes = Task.objects.all().order_by('-post_date')
     
     form = TodoForm()
     if request.method == 'POST':
        form = TodoForm(request.POST)
     if form.is_valid():
            form.save()
            return redirect('home')

  

     return render (request, 'notes.html', {'notes': notes, 'form': form} )


def deletetasks(request, pk):

    
    item = Task.objects.get(id = pk) 

    item.delete()
    return redirect('home')





   