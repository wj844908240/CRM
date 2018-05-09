from django.db import models

from crm.models import UserProfile,Customer
# Create your models here.



class Account(models.Model):
    account = models.OneToOneField(UserProfile,on_delete=models.CASCADE,related_name="stu_account")
    profile = models.OneToOneField(Customer,on_delete=models.CASCADE)





