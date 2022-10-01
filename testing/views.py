from django.shortcuts import render,get_object_or_404
from django.shortcuts import HttpResponse,render,redirect
from .models import pageview,smartbill
from income.models import bill,update,account
from django.views.generic import ListView,DetailView,DeleteView,CreateView,UpdateView
from income.forms import bill_form,updateform
from django.views import View
from .forms import smartbillform
# Create your views here.
def home(request):
	data=pageview()
	context={
	'data':data,
	}
	return render(request,'testindex.html',context)

def page(request):
	context={}
	return render(request,'testpage.html',context)

class BillListView(ListView):
    queryset=bill.objects.all()
    template_name='bill_list.html'
    context_object_name='bills'
    
class BillDetailView(DetailView):
    queryset=bill.objects.all()
    template_name='bill_detail.html'
    context_object_name='bill'
    
class BillCreateView(CreateView):
 
    model=bill
    comment='''
    if doubt:
    	goto "Class-based generic views - flattened index" i.e(django 
    	documentation page and clear your doubts)

    if we declare model and if we have a get_absolute_url() in it
    then it will call that method
    else it will use success_url variable as redirecting path
'''
    queryset=bill.objects.all()
    form_class=bill_form
    template_name='bill_create.html'
    success_url = "./"

    def form_valid(self,form):
    	print(form.cleaned_data)
    	
    	return super().form_valid(form)
    	comment='''
    	#form_valid() is a django reserved function name!

    	#CreateView has a method called 
    	form_valid() through which we send validated forms
    	and then it will save our validated forms!'''
    
class IncomeUpdateView(UpdateView):
	model = bill
	fields = [
		'Name',
		'Amount']
	template_name='bill_create.html'
	success_url='../page2'
	pk_url_kwarg='id'
	comment=''' 
	if doubt:
		visit " https://ccbv.co.uk/projects/Django/1.11/
		django.views.generic.edit/UpdateView/#as_view "
	'''
	def form_valid(self,form):
		return super().form_valid(form)
class deleteview(DeleteView):
	queryset=bill.objects.all()
	template_name='bill_delete.html'
	context_object_name='bills'
	success_url='../page2'
	pk_url_kwarg='id'
	
class view_list(View):
	template_name='account_list.html'
	queryset=account.objects.all()
	context_objects_name='accounts'
	def get(self,request,*args,**kwargs):
		return render(request,self.template_name,context={'accounts':account.objects.all()})

class rawdetail(View):
	template_name='rawdetail.html'
	success_url='../'
	
	def get(self,request,id=None):
		context={}
		if id is not None:
			queryset=get_object_or_404(smartbill,id=id)
			context['data']=queryset
			return render(request,self.template_name,context)
class QuerySetMixin:
	def get_allqueryset(self):
		queryset=smartbill.objects.all()
		return queryset
	def get_onequeryset(self,id):
		queryset=get_object_or_404(smartbill,id=id)
		return queryset
class rawlist(QuerySetMixin,View):
	template_name='rawlist.html'
	success_url='../'
	def get(self,request):
		context={}
		context['data']=self.get_allqueryset()
		return render(request,self.template_name,context)

class rawcreate(View):
	template_name='rawcreate.html'
	success_url='../rawlist'
	def get(self,request):
		form=smartbillform()
		context={
		'form':form,
		}
		return render(request,self.template_name,context)
	def post(self,request):
		form=smartbillform(request.POST)
		context={
		'form':form,
		}
		if form.is_valid():
			form.save()
			print('raw form saved!')
			return redirect(self.success_url)
			
		return render(request,self.template_name,context)

class rawupdate(QuerySetMixin,View):
	template_name='rawupdate.html'
	success_url='../'
	
	def get(self,request,id=None,*args,**kwargs):
		
		if id is not None:

			obj=self.get_onequeryset(id)
			form=smartbillform(instance=obj)

			context={
			'form':form,
			}
			print('id in get : ',id)
			return render(request,self.template_name,context)
	def post(self,request,id=None,*args,**kwargs):
		print('id: ',id)
		if id is not None:
			obj=self.get_onequeryset(id)
			form=smartbillform(request.POST,instance=obj)
			context={
			'form':form,
			}
			
			if form.is_valid():
				form.save()
				print('raw form saved!')
				return redirect(self.success_url)
				
		return render(request,self.template_name,context)

class rawdelete(QuerySetMixin,View):
	
	template_name='rawlist.html'
	
	
	def get(self,request,id=None,*args,**kwargs):
		
		if id is not None:

			obj=self.get_onequeryset(id)
			print('id in get : ',id)
			obj.delete()
			return redirect('../')
	
