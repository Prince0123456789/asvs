from django.shortcuts import render,redirect
from rest_framework.response import Response
from .serializers import UserSignupSerializer, LoginSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt
from .models import UserProfile
# Create your views here.

def loginPage(request):
     return render(request,"asvs_app/login.html")

def signupPage(request):
     return render(request,"asvs_app/signup.html")

@api_view(['POST'])
def userRegistration(request):
    user = request.data.get('user', {})
    if not "signup_from" in user:
        user["signup_from"]="web"
    referral_code = user.pop("referral_code")
    print(referral_code)
    serializer = UserSignupSerializer(data=user)
    if serializer.is_valid(raise_exception=True):
    # print(serializer.data)
        serializer.save()
        user = authenticate(request, username=user["email"], password=user["password"])
        if user is not None:
            login_user = login(request, user)
            print("login_user",login_user)
            # return redirect('home')  # Redirect to a success page
        else:
            pass
        userprofile = UserProfile.objects.create(
             user=user,
             referral_code=referral_code
        )
    return Response(serializer.data, status=status.HTTP_201_CREATED)




@api_view(['POST'])
def UserLogin(request):
        try:
            user = request.data.copy()
            # Notice here that we do not call `serializer.save()` like we did for
            # the registration endpoint. This is because we don't  have
            # anything to save. Instead, the `validate` method on our serializer
            # handles everything we need.
            user = authenticate(request, username=user["email"], password=user["password"])
            if user is not None:
                login_user = login(request, user)
                print("login_user",login_user)
                # return redirect('home')  # Redirect to a success page
            else:
                pass
            serializer = LoginSerializer(user)
            # serializer.is_valid(raise_exception=True)
            # print(serializer.data)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
             return redirect("/")

@api_view(['GET'])
def userLogout(requset):
     user = logout(requset)
     return redirect("/login")


@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def profilePage(request):
     return render(request,"asvs_app/profile.html")