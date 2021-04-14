from django.db import models
import re
import bcrypt

# Create your models here.

class UserManager(models.Manager):
    def RegistrationValidator(self, postData):
        errors = {}
        
        if len(postData['first_name']) <2:
            errors['first_name'] = 'First Name should be greater than 2 characters'
        
        if len(postData['last_name']) <2:
            errors['last_name'] = 'Last Name should be greater than 2 characters'
            
        if len(postData['password']) <8:
            errors['password'] = 'Password should be greater than 8 characters'
            
        UserRegex = re.compile(r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$')
        
        if not UserRegex.match (postData['email']):
            errors['email'] = 'Email is not valid'
            
        email_check = User.objects.filter(email = postData['email']) 
        
        if len(email_check) > 0:
            errors['email_exist'] = 'Email already in use'
            
        if postData['password'] != postData['confirm_password']:
            errors['confirm_password'] = 'Confrim password does not match'
            
        return errors
    
    def LoginValidator(self, postData):
        errors = {}
        login_user = User.objects.filter(email = postData['email'])
        if len(login_user)> 0:
            if bcrypt.checkpw(postData['password'].encode(), login_user[0].password.encode()):
                print ('password matches')
            else:
                errors['password'] = 'Password does not match'
        else:
            errors['email'] = 'There is no user with that email'
        
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 80)
    password = models.CharField (max_length = 32)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField (auto_now = True)
    objects = UserManager()