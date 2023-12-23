from rest_framework import serializers
from .models import GalleryCategory,GalleyImages


class GalleryImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model =GalleyImages
        fields = ["image"]


class GalleryCategorySerializer(serializers.ModelSerializer):
    images = GalleryImagesSerializer(GalleyImages.objects.all(),many=True)
    class Meta:
        model = GalleryCategory
        fields = ["title","description","images"]

