from rest_framework import serializers
from .models import MainPhoto, SubPhoto


class MainPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPhoto
        fields = ['id', 'user_profile', 'file', 'text']


class SubPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubPhoto
        fields = ['id', 'main_photo', 'file', 'text']