from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView,  UpdateView, DetailView, DeleteView
from .models import Task
from .forms import TodoForm
from urllib import request
from django.urls import reverse_lazy

# Create your views here.





def home(request):
     notes = Task.objects.all().order_by('-post_date')
     form = TodoForm()
     if request.method == 'POST':
        form = TodoForm(request.POST)
     if form.is_valid():
            form.save()
            return redirect('home')
     return render (request, 'home.html', { 'form': form, 'notes': notes})


def edittask(request, pk):
   note = Task.objects.get(id = pk)
   if request.method == 'POST':
      form = TodoForm( request.POST, instance=note)
      if form.is_valid():
         form.save()
         return redirect('home')
   return render (request, 'edittask.html', {'form': form})
    

def deletetask(request, pk):  
   note = Task.objects.get(id = pk) 
   note.delete()
   return redirect('home')








   