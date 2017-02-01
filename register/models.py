from django.db import models

# Create your models here.

class UserRegis(models.Model):
    first_name=models.CharField(max_length=120,null=True,blank=True)
    last_name=models.CharField(max_length=120,null=True,blank=True)
    email=models.EmailField()
    contact=models.CharField(max_length=120,null=True,blank=True)
    batch=models.CharField(max_length=120,null=True,blank=True)
    guardian_name=models.CharField(max_length=120,null=True,blank=True)
    guardian_email=models.EmailField()
    guardian_contact=models.CharField(max_length=120,null=True,blank=True)
    username=models.CharField(max_length=120,null=True,blank=True)
    password=models.CharField(max_length=120,null=True,blank=True)
    status=models.CharField(max_length=120,null=True,blank=True)
    picture = models.ImageField(upload_to = 'pictures')

    #photo_upload=models.filefield(upload_to="C:\Users\GURSIMRANJIT\indus_project\register\images")
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)

    def __str__(self) :
        return str(self.username)
