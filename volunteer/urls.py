from django.urls import path
from .views import become_volunteer
urlpatterns = [
    path("volunteer/become_volunteer/",become_volunteer)
]
