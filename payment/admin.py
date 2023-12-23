from django.contrib import admin

# Register your models here.
from .models import CreatePayment,PaymentStatus

admin.site.register(CreatePayment)
admin.site.register(PaymentStatus)