from django.db import models


## django.db package importing module (models)
# Create your models here.

import uuid
class Projects(models.Model):
    title = models.CharField(max_length=255)  # Title field with max length of 255 characters
    description = models.TextField(null = True, blank = True) 
    demo_link = models.CharField(max_length=2000,null = True, blank = True) 
    source_link = models.CharField(max_length=2000, null = True, blank = True) 
    image = models.ImageField(upload_to='project_images/',null = True, blank=True)
    created = models.DateTimeField(auto_now_add=True) 
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key = True, editable = False) 
    tag = models.ManyToManyField('Tag',blank=True) 
    vote_total = models.IntegerField(default = 0, null = True, blank = True) 
    vote_ratio = models.IntegerField(default = 0, null = True, blank = True) 
     # Description field that can hold longer text
    # id field is automatically created as a primary key by Django

    def __str__(self):
        return self.title  # String representation of the model


class Review(models.Model): 
    VOTE_TYPE = (
        ('up','Up Vote'), 
        ('down', 'Down Vote'), 
    ) 
    #owner = 
    project = models.ForeignKey(Projects,on_delete=models.CASCADE) 
    body = models.TextField(null = True, blank = True)  
    value = models.CharField(max_length=200,choices=VOTE_TYPE) 
    created = models.DateTimeField(auto_now_add=True) 
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key = True, editable = False)

    def __str__(self): 
        return self.value



##The ForeignKey field in Django creates a many-to-one relationship. 
# This means that multiple instances of the current model (e.g., Review) 
# can be associated with a single instance of another model (in this case, Item).


class Tag(models.Model) : 
    name = models.CharField(max_length=255) 
    created = models.DateTimeField(auto_now_add=True) 
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key = True, editable = False)

    def __str__(self): 
        return self.name
