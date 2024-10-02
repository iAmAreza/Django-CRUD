from django import forms 
from django.forms import ModelForm 
from .models import Projects 


class ProjectForm(ModelForm): 
    class Meta: 
        model = Projects
        fields = ['title','image','description','demo_link','source_link','tag']  
        # '__all__' if we want to take all the columns 