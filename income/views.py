from django.shortcuts import render,redirect,get_object_or_404
from .forms import incomeform,deleteform,bill_form,updateform
from .models import account,delete,bill,bill_counter
# Create your views here.
def home(request,*args,**kwargs):
	data=account.objects.all()
	total=0
	for i in data:
		print(i.Monthly_salary)
		total+=int(i.Monthly_salary)
	collected=bill.objects.all()
	amount=0
	for i in collected:
		amount+=i.Amount
	print('bill =',amount)
	balance_amount=total-amount
	Flag=True
	if Flag==True:
		if total == 0:
			total='Insufficient!'
			Flag=False
	else:pass
	if Flag==True:
		if total<amount:
			balance_amount='Insufficient'
	else:balance_amount='Insufficient'
	
	

	context={
	'amount':balance_amount,
	'user':request.user,
	'accounts':data,
	'total':total,
	}
	return render(request,'index.html',context)


def delete(request):
	
	if request.method=='POST':
		account_to_remove=deleteform(request.POST)
		context={
		'remove':account_to_remove,
		}
		if account_to_remove.is_valid():
			for i in account.objects.all():
				if i.Company_name.upper()==account_to_remove.cleaned_data['Company_name'].upper() :
					i.delete()
					return redirect('../../')
				
		return render(request,'delete-account.html',context)
	account_to_remove=deleteform()
	context={
	'remove':account_to_remove,
	}
	return render(request,'delete-account.html',context)
def income_update(request):
	if request.method=='POST':
		account_to_update=updateform(request.POST)
		context={
		'account':account_to_update,
		}
		if account_to_update.is_valid():
			for i in account.objects.all():
				if i.Company_name.upper()==account_to_update.cleaned_data['Company_name'].upper() :
					i.Monthly_salary=account_to_update.cleaned_data['Monthly_salary']
					i.save()
					if i.Monthly_salary==account_to_update.cleaned_data['Monthly_salary']:
						print('changed!')
						return redirect('../../')
					else:print('Not changed!')
				
		return render(request,'income-update.html',context)
	account_to_update=updateform()
	context={
	'account':account_to_update,
	}
	
	return render(request,'income-update.html',context)
def balance(request):
	data=bill.objects.all()
	if len(data)<1:
		data='No Bills'
	context={
	'data':data,
	}
	return render(request,'more-info.html',context)
def dynamic_balance(request,data):
	info=get_object_or_404(bill,id=data)
	more=bill.objects.all()
	context={
	'data':info,
	'more':more,
	}
	return render(request,'absolute_url.html',context)
def create_account(request):
	if request.method=='POST':
		form=incomeform(request.POST)
		context={
		'form':form,
		}
		if form.is_valid()==True:
			print('is_valid is True')
			if form.cleaned_data!='{}':
				print('cleaned_data verified')
				form.save()
				print('data is saved!')
				return redirect('../../')
		return render(request,'create_account.html',context)
	form=incomeform()
	context={
	'form':form,
	}
	return render(request,'create_account.html',context)

def billentry(request):
	
	if request.method=='POST':
		form=bill_form(request.POST)
		data=bill.objects.all()
		if len(data)<1:
			data='No Bills'
		context={
		'form':form,
		'result':data,
		}
		if form.is_valid():
			if form.cleaned_data!='{}':
				form.save()
				

				return redirect('./')
		return render(request,'bills.html',context)

	form=bill_form()
	data=bill.objects.all()
	if len(data)<1:
		data='No Bills'
	context={
	'form':form,
	'result':data,
	}
	return render(request,'bills.html',context)
def deletebill(request,data):

	for i in bill.objects.all():
		if i.Name.lower()==data.lower():
			i.delete()
			return redirect('./')
