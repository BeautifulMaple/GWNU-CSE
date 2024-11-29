#model.py DB를 저장할 데이터 구조와 필드 정의하는 파일
# 또 클래스가 생성되고 저장되는 곳이기도 함
from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.validators import EmailValidator

class UserProfile(models.Model):
    email = models.EmailField(unique=True, blank=True)  # 이메일
    password = models.CharField(max_length=128)  # 비밀번호 해시 저장
    nickname = models.CharField(max_length=50, unique=True, blank=True)  # 닉네임 (유일해야 하는 경우)
    real_name = models.CharField(max_length=20, null=True, blank=True)  # 실명

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        # 비밀번호가 해시되지 않은 경우에만 해시 처리
        if not self.pk or not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)



class MainPhoto(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='main_photos')
    file = models.FileField(upload_to='main_photos/')
    text = models.TextField(blank=True, null=True)  # 설명 텍스트
    

class SubPhoto(models.Model):
    main_photo = models.ForeignKey(MainPhoto, on_delete=models.CASCADE, related_name='sub_photos')
    file = models.ImageField(upload_to='sub_photos/')
    text = models.TextField(blank=True, null=True)  # 설명 텍스트


