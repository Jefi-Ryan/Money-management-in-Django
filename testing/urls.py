from django.contrib import admin
from django.urls import path
from .views import BillListView,BillDetailView,BillCreateView,IncomeUpdateView,deleteview,view_list
from .views import rawdetail,rawlist,rawcreate,rawupdate,rawdelete
from testing import views

app_name='testing'
urlpatterns=[
	path('',views.home,name='testhome'),
	path('page1',views.page,name='testpage'),
	path('page2',BillListView.as_view()),
	path('page3/<int:pk>',BillDetailView.as_view()),
	path('page4/',BillCreateView.as_view()),
	path('page5/<int:id>',IncomeUpdateView.as_view(),name='dynamic-page5'),
	path('page6/<int:id>',deleteview.as_view(),name='dynamic-page6'),
	path('page7/',view_list.as_view(template_name='account_list.html'),name='dynamic-page6'),
	path('rawdetail/<int:id>',rawdetail.as_view(),name='detail'),
	path('rawlist/',rawlist.as_view(),name='list'),
	path('rawlist/description/<int:id>',rawdetail.as_view(),name='list'),
	path('rawcreate/',rawcreate.as_view(),name='create'),
	path('rawlist/update/<int:id>',rawupdate.as_view(),name='update'),
	path('rawlist/delete/<int:id>',rawdelete.as_view(),name='delete'),
	
]