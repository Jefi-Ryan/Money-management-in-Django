from django.contrib import admin
from .models import account,delete,bill,bill_counter,update
# Register your models here.
admin.site.register(account)
admin.site.register(delete)
admin.site.register(bill)
admin.site.register(bill_counter)
admin.site.register(update)