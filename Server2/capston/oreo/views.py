from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout
from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ObjectDoesNotExist
from .models import UserProfile
import json, random, string

# 메인 홈 화면
def MainHome(request):
    return render(request, 'MainHome.html')

# 로그인 후 홈 화면
def LoginHome_view(request):
    return render(request, 'LoginHome.html')

# 로그인 페이지
def login_view(request):
    return render(request, 'login.html')

# ID 찾기 페이지
def idfind_view(request):
    return render(request, 'idfind.html')

# PW 찾기 페이지
def pwfind_view(request):
    return render(request, 'pwfind.html')

# 회원가입 단계 1 페이지
def signup_view(request):
    return render(request, 'signup.html')

# 회원가입 단계 2 페이지
def signup1_view(request):
    return render(request, 'signup1.html')

# 파일 업로드 페이지
def uplode_view(request):
    return render(request, 'uplode.html')

# QR 스캔 페이지
def QRscan_view(request):
    return render(request, 'QRscan.html')

# 로그아웃 처리
def logout_view(request):
    logout(request)
    return redirect('MainHome')

# 회원가입 1단계: 사용자 정보 저장
@csrf_exempt
def register_user_step1(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # 클라이언트에서 전송된 JSON 데이터 파싱
            user_id = data.get('user_id')  # user_id 필드
            email = data.get('email')      # email 필드
            password = data.get('password')  # password 필드
            real_name = data.get('real_name')  # real_name 필드

            # 필수 필드가 모두 존재하는지 확인
            if not all([user_id, email, password, real_name]):
                return JsonResponse({'error': 'All fields are required (user_id, email, password, real_name)'}, status=400)

            # 사용자 생성
            user = UserProfile.objects.create(
                user_id=user_id,
                email=email,
                password=make_password(password),  # 비밀번호 해시화
                real_name=real_name,
            )

            return JsonResponse({'message': 'Step 1 completed successfully', 'user_id': user.user_id}, status=201)
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


# 아이디 중복
def check_id(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_id = data.get('user_id')

            if not user_id:
                return JsonResponse({'error': '아이디를 입력해주세요.'}, status=400)

            # 아이디 중복 확인
            is_duplicate = UserProfile.objects.filter(user_id=user_id).exists()

            return JsonResponse({'is_duplicate': is_duplicate})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

# 이메일 중복확인
def check_email(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')

            if not email:
                return JsonResponse({'error': '이메일을 입력해주세요.'}, status=400)

            # 이메일 중복 확인
            is_duplicate = UserProfile.objects.filter(email=email).exists()

            return JsonResponse({'is_duplicate': is_duplicate})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

from django.core.cache import cache
# 이메일 전송 코드
def send_verification_code(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')

            if not email:
                return JsonResponse({'error': '이메일을 입력해주세요.'}, status=400)

            # 인증 코드 생성 (6자리 숫자)
            verification_code = ''.join(random.choices(string.digits, k=6))

            # 인증 코드를 캐시에 저장 (유효 시간: 5분)
            cache.set(email, verification_code, timeout=300)  # 300초 = 5분

            # 이메일 발송
            send_mail(
                '인증 코드',
                f'다음 인증 코드를 입력하세요: {verification_code}',
                'xorua4510@naver.com',  # 발신자 이메일
                [email],
                fail_silently=False,
            )

            return JsonResponse({'message': '인증 코드가 발송되었습니다.'}, status=200)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def verify_code(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            code = data.get('code')

            if not email or not code:
                return JsonResponse({'error': 'Email과 인증 코드를 입력해주세요.'}, status=400)

            # 캐시에서 인증 코드 가져오기
            cached_code = cache.get(email)
            if cached_code is None:
                return JsonResponse({'is_valid': False, 'error': '인증 코드가 만료되었습니다.'}, status=400)

            # 인증 코드 비교
            if cached_code == code:
                return JsonResponse({'is_valid': True}, status=200)
            else:
                return JsonResponse({'is_valid': False}, status=400)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)



# 회원가입 2단계: 닉네임 설정
@csrf_exempt
def register_user_step2(request):
    """
    2단계: 닉네임을 입력받아 기존 사용자 업데이트.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # 클라이언트에서 전송된 JSON 데이터 파싱
            user_id = data.get('user_id')  # user_id로 사용자 찾기
            nickname = data.get('nickname')

            if not all([user_id, nickname]):
                return JsonResponse({'error': 'Both user_id and nickname are required'}, status=400)

            # user_id로 사용자 검색
            try:
                user = UserProfile.objects.get(user_id=user_id)  # user_id로 찾기
            except ObjectDoesNotExist:
                return JsonResponse({'error': 'User not found'}, status=404)

            # 닉네임 업데이트
            user.nickname = nickname
            user.save()

            # 성공 응답
            return JsonResponse({'message': 'Step 2 completed successfully', 'user_id': user.user_id}, status=200)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

