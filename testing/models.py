from django.db import models
from django.shortcuts import reverse
# Create your models here.
class pageview(models.Model):
	def page(self):
		return reverse('testing:testpage',kwargs={})

class smartbill(models.Model):
	Name=models.CharField(max_length=120)
	Amount=models.IntegerField()
	Description=models.TextField(max_length=500)
