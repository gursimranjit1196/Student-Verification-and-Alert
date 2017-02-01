from django.db import models

# Create your models here.

class Timetable(models.Model):
    Daynumber=models.CharField(max_length=120,null=True,blank=True)
    Day=models.CharField(max_length=120,null=True,blank=True)
    T9AM=models.CharField(max_length=120,null=True,blank=True)
    T10AM=models.CharField(max_length=120,null=True,blank=True) 
    T11AM=models.CharField(max_length=120,null=True,blank=True)
    
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)

    def __str__(self):
        return str(self.Daynumber)+"--"+str(self.Day)+"--"+str(self.T9AM)+"--"+str(self.T10AM)+"--"+str(self.T11AM)
