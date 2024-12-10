from django.db import models
from django.contrib.auth.hashers import make_password
import os
from os.path import exists
import uuid
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils import timezone  # 현재 날짜를 가져오기 위해 추가
from django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # UserProfile이 있는 경우에만 저장
    if hasattr(instance, 'userprofile'):
        instance.userprofile.save()

def user_main_photo_path(instance, filename):
    """사용자 이메일 기반 main_photos 경로 생성 및 파일 이름 충돌 방지"""
    email = instance.user_profile.email.lower().replace('@', '_').replace('.', '_')
    ext = filename.split('.')[-1]
    unique_filename = f"{uuid.uuid4().hex}.{ext}"  # 유니크한 파일 이름 생성
    return os.path.join(email, 'main_photos', unique_filename)

def user_sub_photo_path(instance, filename):
    """사용자 이메일 기반 sub_photos 경로 생성 및 파일 이름 충돌 방지"""
    email = instance.main_photo.user_profile.email.lower().replace('@', '_').replace('.', '_')
    ext = filename.split('.')[-1]
    unique_filename = f"{uuid.uuid4().hex}.{ext}"  # 유니크한 파일 이름 생성
    return os.path.join(email, 'sub_photos', unique_filename)



class UserProfile(models.Model):
    email = models.EmailField(unique=True, blank=True)
    password = models.CharField(max_length=128)
    nickname = models.CharField(max_length=50, unique=True, blank=True)
    real_name = models.CharField(max_length=20, null=True, blank=True)
    kakao_id = models.CharField(max_length=50, unique=True, null=True)
    urls = models.JSONField(default=list)
    
    def __str__(self):
        return self.email

    def set_password(self, raw_password):
        """비밀번호를 해시화하여 저장"""
        from django.contrib.auth.hashers import make_password
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """비밀번호가 일치하는지 확인"""
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password, self.password)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class MainPhoto(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='main_photos')
    file = models.FileField(upload_to='main_photos/')
    text = models.TextField(blank=True, null=True)  # 설명 텍스트

    def delete(self, *args, **kwargs):
        # 파일도 삭제
        if self.file:
            self.file.delete(save=False)
        super().delete(*args, **kwargs)


class SubPhoto(models.Model):
    main_photo = models.ForeignKey(MainPhoto, on_delete=models.CASCADE, related_name='sub_photos')
    file = models.ImageField(upload_to='sub_photos/')
    text = models.TextField(blank=True, null=True)  # 설명 텍스트

    def delete(self, *args, **kwargs):
        # 파일도 삭제
        if self.file:
            self.file.delete(save=False)
        super().delete(*args, **kwargs)