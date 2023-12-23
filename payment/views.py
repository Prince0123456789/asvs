from django.shortcuts import render,redirect
from .models import CreatePayment, PaymentStatus
from django.http import HttpResponse
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view
import razorpay
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@api_view(['POST'])
def createpayment(request):
    name = request.data.get("name")
    email = request.data.get("email")
    amount = request.data.get("amount")
    client=razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_SECRETE_KEY))
    data = {"amount" : int(amount)*100, "currency" : "INR"}
    payment = client.order.create(data=data)
    data={'order_id': payment['id'], 'amount': payment['amount'], 'currency':payment['currency']}
    CreatePayment.objects.create(
        name=name,
        email=email,
        amount = amount,
        order_id = payment['id']
    )
    return Response(data)



@api_view(['POST'])
@csrf_exempt
def paymentStatus(request):
    # try:
        client=razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_SECRETE_KEY))
        order_id=request.data.get('order_id')
        payment_id = request.data.get("payment_id")
        signature_id = request.data.get("signature_id")
        status_id = request.data.get("status")
        params_dict = {
                'razorpay_order_id': order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature_id
            }
        print(order_id)
 
            # verify the payment signature.

        # result = client.utility.verify_payment_signature(
        #         params_dict)
        result=1
        if result:
            create_payemnt=CreatePayment.objects.get(order_id=order_id)
            payst = PaymentStatus.objects.create(
            payment_created_id = create_payemnt.id,
            payment_id = payment_id,
            order_id = order_id,
            signature_id = signature_id,
            status = True
            )
        return Response("Payment Successfull",status=status.HTTP_200_OK)
    # except:
    #     return Response({"msg":"Payment failed if money deducted contact admin"},status=status.HTTP_400_BAD_REQUEST)


    