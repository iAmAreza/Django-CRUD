from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import Projects
from django.db import transaction

from .forms import ProjectForm

 



def projects(request):
    projects = Projects.objects.all()
    context = {
    'projects' : projects
    }
    # Render the 'projects.html' template with the context
    return render(request, 'projects/projects.html', context)

 
def createProjectForm(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('projects')  
    
    context = {'form': form}
    
    return render(request, 'projects/project-form.html', context)





def updateProjectForm(request,pk): 
    project = Projects.objects.get(id = pk) 
    form = ProjectForm(instance = project)  
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('projects')  # Redirect after saving
        
    
    context = {'form': form}

    return render(request, 'projects/project-form.html', context)





def deleteProject(request, pk):
    # Get the specific project object
    project = Projects.objects.get(id=pk)

    if request.method == 'POST':  # If the request method is POST, proceed with deletion
        project.delete()
        return redirect('projects')  # Redirect to the projects list page after deletion

    # If the request is GET, display the confirmation page
    context = {'project': project}
    return render(request, 'projects/delete-project.html', context)


def project(request,pk): 
    object = Projects.objects.get(id = pk) 
    
    return render(request, 'projects/single-project.html',{'object' : object})   