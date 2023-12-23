from django.shortcuts import render,redirect
from .models import ContactUs
# Create your views here.
def index(request):
    return redirect("/home")


def contact_us(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        ContactUs.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        return redirect("/home")