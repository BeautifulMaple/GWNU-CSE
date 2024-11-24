from django.shortcuts import render

# Create your views here.

def MainHome(request):
    return render(request, 'MainHome.html')

def LoginHome_view(request):
    return render(request, 'LoginHome.html')

def login_view(request):
    return render(request, 'login.html')

def idfind_view(request):
    return render(request, 'idfind.html')

def pwfind_view(request):
    return render(request, 'pwfind.html')

def signup_view(request):
    return render(request, 'signup.html')

def signup1_view(request):
    return render(request, 'signup1.html')

def uplode_view(request):
    return render(request, 'uplode.html')

def QRscan_view(request):
    return render(request, 'QRscan.html')

from django.shortcuts import redirect
from django.contrib.auth import logout

def logout_view(request):
    """
    로그아웃 처리 후 MainHome으로 리다이렉트
    """
    logout(request)  # 사용자 세션 종료
    return redirect('MainHome')  # MainHome 페이지로 리다이렉트
