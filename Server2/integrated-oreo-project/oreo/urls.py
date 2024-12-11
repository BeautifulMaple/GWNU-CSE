from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import register_user_step1, register_user_step2
from .views import check_email, send_verification_code
from .photo_view import MainPhotoView, SubPhotoView

urlpatterns = [
    path('', views.mainhome, name='mainhome'),
    
    # 로그인 관련 URL 패턴
    path('login/', views.login_view, name='login'),
    path('login_data/', views.login_data, name='login_data'),
    path('process_login/', views.process_login, name='process_login'),
    path('logout/', views.logout_view, name='logout'),
    path('loginhome/', views.loginhome_view, name='loginhome'),

    # 회원가입 관련
    path('signup/', views.signup_view, name='signup'),
    path('signup1/', views.signup1_view, name='signup1'),
    
    # ID/PW 찾기
    path('idfind/', views.idfind_view, name='idfind'),
    path('register_user/step1/find_id/', views.find_id, name='find_id'),
    path('pwfind/', views.pwfind_view, name='pwfind'),
    path('resetpassword/', views.resetpassword_view, name='resetpassword'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('register_user/step1/find_pw/', views.find_pw, name='find_pw'),
    
    # 사진 업로드
    path('uplode/', views.uplode_view, name='uplode'),
    path('uplode_photo/', views.uplode_photo, name='uplode_photo'),
    path('api/main_photos/', MainPhotoView.as_view(), name='main_photo_api'),
    path('api/album_data/', views.album_data, name='album_data'),
    path('album_data/', views.album_data, name='album_data'),
    path('get_user_photos/', views.get_user_photos, name='get_user_photos'),

    # QR 관련
    path('qrscan/', views.qrscan_view, name='qrscan'),
    path('save_qr_url/<int:user_id>/', views.save_qr_url, name='save_qr_url'),

    # 회원가입 단계
    path('register_user/step1/', register_user_step1, name='register_user_step1'),
    path('register_user/step2/', register_user_step2, name='register_user_step2'),
    
    # 이메일 인증
    path('register_user/step1/check_email/', check_email, name='check_email'),
    path('register_user/step1/send_verification_code/', send_verification_code, name='send_verification_code'),
    path('register_user/step1/verify_code/', views.verify_code, name='verify_code'),

    # 사진 관련 API
    path('main-photo/<int:pk>/', MainPhotoView.as_view(), name='main-photo-detail'),
    path('main-photo/user/<int:user_id>/', MainPhotoView.as_view(), name='main-photo-by-user'),
    path('sub-photo/<int:pk>/', SubPhotoView.as_view(), name='sub-photo-detail'),
    path('sub-photo/main/<int:main_photo_id>/', SubPhotoView.as_view(), name='sub-photo-by-main'),
<<<<<<< HEAD
    path('delete_photo/', views.delete_photo, name='delete_photo'),
=======
>>>>>>> origin/develop_KTG

    # 소셜 로그인
    path('accounts/', include('allauth.urls')),
    path('accounts/kakao/login/', views.kakao_login, name='kakao_login'),
    path('accounts/kakao/callback/', views.kakao_callback, name='kakao_callback'),

    # 회원가입 API
    path('register_user/', views.register_user, name='register_user'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# 정적 및 미디어 파일 처리
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)