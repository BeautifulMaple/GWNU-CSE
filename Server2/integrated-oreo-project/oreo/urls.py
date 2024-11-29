from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import register_user_step1, register_user_step2
from .views import  check_email, send_verification_code


urlpatterns = [
    path('', views.MainHome, name='MainHome'),
    path('login/', views.login_view, name='login'),
    path('login/process/', views.process_login, name='process_login'),  # 이름 변경 반영


    path('signup/', views.signup_view, name='signup'),
    path('signup1/', views.signup1_view, name='signup1'),

    path('idfind/', views.idfind_view, name='idfind'),
    path('register_user/step1/find_id/', views.find_id, name='find_id'),

    path('pwfind/', views.pwfind_view, name='pwfind'),
    path('resetpassword/', views.resetpassword_view, name='resetpassword'),
    path('reset_password/', views.reset_password, name='reset_password'),

    path('register_user/step1/find_pw/', views.find_pw, name='find_pw'),


    path('uplode/', views.uplode_view, name='uplode'),
    path('LoginHome/', views.LoginHome_view, name='LoginHome'),
    path('QRscan/', views.QRscan_view, name='QRscan'),
    path('logout/', views.logout_view, name='logout'),

    # 회원가입 과정
    path('register_user/step1/', register_user_step1, name='register_user_step1'), # 회원가입
    path('register_user/step2/', register_user_step2, name='register_user_step2'), # 닉네임
    
    # 중복 체크 및 인증 코드 발송
    path('register_user/step1/check_email/', check_email, name='check_email'),  # 이메일 중복 확인 추가
    path('register_user/step1/send_verification_code/', send_verification_code, name='send_verification_code'),
    path('register_user/step1/verify_code/', views.verify_code, name='verify_code'),


]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# 정적 및 미디어 파일 처리
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)