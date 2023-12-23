from django.shortcuts import render,redirect
from .models import Volunteer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["POST"])
def become_volunteer(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        why_to_become_volunteer = request.POST.get("why_to_become_volunteer")

        Volunteer.objects.create(
            name=name,
            email=email,
            why_to_become_volunteer = why_to_become_volunteer
        )

        return redirect("/home")