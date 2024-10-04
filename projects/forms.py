from django import forms 
from django.forms import ModelForm 
from .models import Projects 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class ProjectForm(ModelForm): 
    class Meta: 
        model = Projects
        fields = ['title','image','description','demo_link','source_link','tag']  
        # '__all__' if we want to take all the columns  



class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150, 
        widget=forms.TextInput(attrs={
            'class': 'bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none',
            'placeholder': 'Enter your email'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none',
            'placeholder': 'Enter your password'
        })
    )



class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'password1': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)  # Fix: use SignUpForm, not CustomUserCreationForm
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None  # Remove help text for these fields