from django.db import models
from django.shortcuts import reverse
from datetime import datetime
# Create your models here.
class account(models.Model):
	Company_name=models.CharField(max_length=120)
	Monthly_salary=models.IntegerField()

	def get_absolute_url(self):
		return reverse('testing:dynamic-page5',kwargs={'pk':self.id})

class delete(models.Model):
	Company_name=models.CharField(max_length=120)

class update(models.Model):
	Company_name=models.CharField(max_length=120)
	Monthly_salary=models.IntegerField()


	
class bill(models.Model):
	Name=models.CharField(max_length=120)
	Amount=models.IntegerField()
	def geturl(self):
		return f'{self.id}'
	def getdetail(self):
		return reverse('income:bill-dynamic',kwargs={'data':self.id})

class bill_counter(models.Model):
	count=models.IntegerField()
