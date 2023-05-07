from django import forms 

from .models import Task


class TodoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('newtasks','priority')


        widgets = {
           
            'newtasks': forms.TextInput(attrs = {'class': 'form-control'}),
        }