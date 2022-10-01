from django import forms

from django.forms import ValidationError
from .models import account,delete,bill,bill_counter,update

class incomeform(forms.ModelForm):
	class Meta():
		model=account
		fields=[
		'Company_name',
		'Monthly_salary',
		]

	def clean_Company_name(self,*args,**kwargs):
		data=self.cleaned_data['Company_name']
		print('Entered:',data)
		for i in account.objects.all():
			print(i.Company_name)
			if i.Company_name.lower()==data.lower():
				print('matched in pre-check')
				raise ValidationError('Company name already exists!')
			if i.Company_name.upper()==data.upper():
				print('matched in pre-check')
				raise ValidationError('Company name already exists!')
			if True:
				data=data.upper()
		return data
class deleteform(forms.ModelForm):
	class Meta():
		model=delete
		fields=[
		'Company_name',
		]
	def clean_Company_name(self,*args,**kwargs):
		data=self.cleaned_data['Company_name']
		print('Entered:',data)
		for i in account.objects.all():
			print(i.Company_name)
			if i.Company_name.lower()==data.lower():
				print('matched in pre-check')
				return data
			if i.Company_name.upper()==data.upper():
				print('matched in pre-check')
				return data
		print('not matched in pre-check')
		raise ValidationError('Company name not exist!')
	
class bill_form(forms.ModelForm):
	class Meta():
		model=bill
		fields=[
		'Name',
		'Amount']
	Name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Bill name'}),label='')
	Amount=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Amount'}),label='')
	def clean_Name(self,*args,**kwargs):
		data=self.cleaned_data['Name']
		if len(data)<1:
			raise ValidationError('Please fill this field')
		return data
	def clean_Amount(self,*args,**kwargs):
		data=self.cleaned_data['Amount']
		if data<1:
			raise ValidationError('Please fill this field')
		return data

class updateform(forms.ModelForm):
	class Meta():
		model=update
		fields=[
		'Company_name',
		'Monthly_salary',]
	def clean_Company_name(self,*args,**kwargs):
		data=self.cleaned_data['Company_name']
		print('Entered:',data)
		for i in account.objects.all():
			print(i.Company_name)
			if i.Company_name.lower()==data.lower():
				print('matched in pre-check')
				return data
			if i.Company_name.upper()==data.upper():
				print('matched in pre-check')
				return data
		print('not matched in pre-check')
		raise ValidationError('Company name not exist!')
		



