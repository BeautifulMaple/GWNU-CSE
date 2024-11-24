from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.MainHome, name='MainHome'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('pwfind/', views.pwfind_view, name='pwfind'),
    path('idfind/', views.idfind_view, name='idfind'),
    path('signup1/', views.signup1_view, name='signup1'),
    path('uplode/', views.uplode_view, name='uplode'),
    path('LoginHome/', views.LoginHome_view, name='LoginHome'),
    path('QRscan', views.QRscan_view, name='QRscan'),
    path('logout/', views.logout_view, name='logout'),  # 로그아웃 경로 추가


    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
