from django.urls import path 
from . import views 
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.projects,name='projects'), 
    path('project/<str:pk>/',views.project, name = 'project-detail'), 
    path('createform/',views.createProjectForm, name = 'createProjectForm'),  
    path('updateproject/<str:pk>', views.updateProjectForm, name = 'update-project-form'),  
    path('delete-project/<str:pk>/', views.deleteProject, name='delete-project'), 
    path('login/', views.login_view,name='login'), 
    path('signup/', views.signup_view, name = 'signup'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login.html'), name='logout'),
]



