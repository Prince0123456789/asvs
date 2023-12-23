from .views import index,contact_us
from django.urls import path

urlpatterns=[

    path('',index,name='index'),
    path("contact_us/",contact_us)
]