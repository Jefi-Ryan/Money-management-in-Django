from django.contrib import admin
from django.urls import path,include
from income import views
app_name='income'
urlpatterns = [
    path('more-info/',views.balance,name='balance'),
    path('income-update/',views.income_update,name='income-update'),
    path('create_account/',views.create_account,name='account'),
    path('delete_account/',views.delete,name='account'),
    path('bill/',views.billentry,name='bills'),
    path('bill/delete-<str:data>',views.deletebill,name='bill-delete'),
    path('more-info/<int:data>',views.dynamic_balance,name='bill-dynamic'),
    
]