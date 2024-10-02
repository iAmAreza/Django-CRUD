from django.urls import path 
from . import views 
urlpatterns = [
    path('', views.projects,name='projects'), 
    path('project/<str:pk>/',views.project, name = 'project-detail'), 
    path('createform/',views.createProjectForm, name = 'createProjectForm'),  
    path('updateproject/<str:pk>', views.updateProjectForm, name = 'update-project-form'),  
    path('delete-project/<str:pk>/', views.deleteProject, name='delete-project'),
]



