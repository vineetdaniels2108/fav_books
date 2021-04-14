from django.db import models
from loginapp.models import * 


# Create your models here.

class BookManager(models.Manager):
    def BookValidator(self, postData):
        errors = {}
        
        if len(postData['title']) == 0:
            errors['title'] = 'Please enter a valid Title'
            
        if len(postData['desc']) <=5 :
            errors['desc'] = 'Please enter a valid description'
        
        return errors

class Books(models.Model):
    title = models.CharField(max_length=80)
    desc = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name='user_upload', on_delete = models.CASCADE)
    liked_by = models.ManyToManyField(User, related_name='liked_users')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()
