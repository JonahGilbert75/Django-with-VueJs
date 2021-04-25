from django.db import models

# Create your models here.


class Job(models.Model):
    
    Company_name= models.CharField(max_length=100)
    Title= models.CharField(max_length=100)
    Job_Nature= models.TextField(max_length=250)
    Salary= models.IntegerField()
    No_of_post =models.IntegerField()
    Name= models.CharField(max_length=100,default=1,blank=False,null=False)

    

    def __str__(self):
        return self.Company_name

    class Meta:
        ordering=['Company_name']





    