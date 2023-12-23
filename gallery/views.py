from django.shortcuts import render
from rest_framework.response import Response
from .models import GalleryCategory
from .serilalizers import GalleryCategorySerializer
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def allGalleryImages(request):
    serializer = GalleryCategorySerializer(GalleryCategory.objects.all(),many=True)
    return Response(serializer.data)