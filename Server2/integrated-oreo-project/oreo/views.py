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
from django.contrib.auth.hashers import check_password
from .models import UserProfile
import json, random, string
from django.contrib.auth import authenticate, login


# 메인 홈 화면
def MainHome(request):
    return render(request, 'MainHome.html')

# 로그인 후 홈 화면
def LoginHome_view(request):
    return render(request, 'LoginHome.html')

# 로그인 페이지
def login_view(request):
    return render(request, 'login.html')

from django.contrib.auth import authenticate, login

def process_login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # JSON 데이터 파싱
            email = data.get('email')  # 클라이언트에서 보낸 email
            password = data.get('password')  # 클라이언트에서 보낸 password

            # 사용자 인증
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)  # Django 로그인 세션 활성화
                return JsonResponse({'success': True})  # 성공 응답
            else:
                return JsonResponse({'error': '아이디 또는 비밀번호가 일치하지 않습니다.'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': '유효하지 않은 요청입니다.'}, status=400)
    return JsonResponse({'error': '잘못된 요청입니다.'}, status=400)

# ID 찾기 페이지
def idfind_view(request):
    return render(request, 'idfind.html')

# 아이디 찾기 (이메일 인증 코드 확인 후 아이디 반환)
def find_id(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get('name')  # 클라이언트에서 받은 이름
        email = data.get('email')  # 클라이언트에서 받은 이메일
        code = data.get('code')  # 사용자로부터 입력받은 인증 코드

        if not all([name, email, code]):
            return JsonResponse({"error": "모든 필드를 입력해주세요."}, status=400)

        # 인증 코드 확인 (캐시에서 가져오기)
        cached_code = cache.get(email)
        if cached_code is None:
            return JsonResponse({"error": "인증 코드가 만료되었습니다."}, status=400)

        # 인증 코드 비교
        if cached_code != code:
            return JsonResponse({"error": "인증 코드가 일치하지 않습니다."}, status=400)

        # 사용자 검색
        try:
            user = UserProfile.objects.get(real_name=name, email=email)  # 'name'을 'real_name'으로 변경
            return JsonResponse({"success": True, "email": user.email})  # user_id 반환
        except ObjectDoesNotExist:
            return JsonResponse({"error": "사용자를 찾을 수 없습니다."}, status=404)



# PW 찾기 페이지
def pwfind_view(request):
    return render(request, 'pwfind.html')

# 재설정
def resetpassword_view(request):
    return render(request, 'resetpassword.html')

@csrf_exempt  # CSRF 보호를 비활성화 (필요시 수정)
def reset_password(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            new_password = body.get('password')

            # 비밀번호 유효성 검사 (예: 최소 길이 확인)
            if not new_password or len(new_password) < 8:
                return JsonResponse({'error': '비밀번호는 최소 8자리 이상이어야 합니다.'}, status=400)

            # 비밀번호 변경 로직 (예: 사용자 인증 및 저장)
            # 예제 코드
            # user = User.objects.get(email=request.user.email)  # 사용자 인증 로직 필요
            # user.set_password(new_password)
            # user.save()

            return JsonResponse({'message': '비밀번호가 성공적으로 변경되었습니다.'})
        except json.JSONDecodeError:
            return JsonResponse({'error': '잘못된 데이터 형식입니다.'}, status=400)
    return JsonResponse({'error': '허용되지 않은 요청입니다.'}, status=405)


# 비밀번호 찾기 (이메일 인증 코드 확인 후 아이디 반환)
def find_pw(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get('name')  # 클라이언트에서 받은 이름
        email = data.get('email')  # 클라이언트에서 받은 이메일
        code = data.get('code')  # 사용자로부터 입력받은 인증 코드

        if not all([name, email, code]):
            return JsonResponse({"error": "모든 필드를 입력해주세요."}, status=400)

        # 인증 코드 확인 (캐시에서 가져오기)
        cached_code = cache.get(email)
        if cached_code is None:
            return JsonResponse({"error": "인증 코드가 만료되었습니다."}, status=400)

        # 인증 코드 비교
        if cached_code != code:
            return JsonResponse({"error": "인증 코드가 일치하지 않습니다."}, status=400)

        # 사용자 검색
        try:
            user = UserProfile.objects.get(real_name=name, email=email)  # 'name'을 'real_name'으로 변경
            return JsonResponse({"success": True, "password": user.password})  # 비밀번호 반환
        except ObjectDoesNotExist:
            return JsonResponse({"error": "사용자를 찾을 수 없습니다."}, status=404)


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

# 회원가입 1단계: 사용자 정보 저장
def register_user_step1(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')
            real_name = data.get('real_name')

            if not all([email, password, real_name]):
                return JsonResponse({'error': '모든 필드를 입력해야 합니다.'}, status=400)

            # 사용자 생성
            user = UserProfile.objects.create(
                email=email,
                password=make_password(password),  # 비밀번호 해시화
                real_name=real_name,
            )
            return JsonResponse({'message': '회원가입 1단계 완료', 'email': user.email}, status=201)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': '잘못된 요청입니다.'}, status=405)


# 회원가입 2단계: 닉네임 설정
@csrf_exempt
def register_user_step2(request):
    """
    2단계: 닉네임을 입력받아 기존 사용자 업데이트.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # 클라이언트에서 전송된 JSON 데이터 파싱
            email = data.get('email')  # email로 사용자 찾기
            nickname = data.get('nickname')

            if not all([email, nickname]):
                return JsonResponse({'error': 'Both email and nickname are required'}, status=400)

            # email로 사용자 검색
            try:
                user = UserProfile.objects.get(email=email)  # email로 찾기
            except ObjectDoesNotExist:
                return JsonResponse({'error': 'User not found'}, status=404)

            # 닉네임 업데이트
            user.nickname = nickname
            user.save()

            # 성공 응답
            return JsonResponse({'message': 'Step 2 completed successfully', 'user_email': user.email}, status=200)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
