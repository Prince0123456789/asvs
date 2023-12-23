from django.urls import path
from .views import allGalleryImages

urlpatterns = [
    path("gallery/allgallerydata/",allGalleryImages)
]
