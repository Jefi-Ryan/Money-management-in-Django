from django import forms
from django.forms import ValidationError
from .models import smartbill

class smartbillform(forms.ModelForm):
	class Meta():
		model=smartbill
		fields=[
		'Name',
		'Amount',
		'Description']
