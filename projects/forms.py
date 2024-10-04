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
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user