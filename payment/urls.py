from django.urls import path
from .views import createpayment,paymentStatus


urlpatterns = [
    path("createpayment/",createpayment),
    path("paymentstatus/",paymentStatus)
]
