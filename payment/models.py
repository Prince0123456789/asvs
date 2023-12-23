from django.db import models


class CreatePayment(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    order_id = models.CharField(max_length=255)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    

class PaymentStatus(models.Model):
    payment_created = models.ForeignKey(CreatePayment,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    payment_id = models.CharField(max_length=255)
    signature_id = models.CharField(max_length=255)
    order_id = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return str(self.payment_created)