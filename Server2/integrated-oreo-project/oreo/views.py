# 표준 라이브러리
import json
import random
import string
import requests
<<<<<<< HEAD
import logging
=======
>>>>>>> origin/develop_KTG

# Django 기본 라이브러리
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.core.mail import send_mail
from django.core.validators import URLValidator
<<<<<<< HEAD
from django.contrib.auth.hashers import make_password, check_password
=======
from django.contrib.auth.hashers import make_password
>>>>>>> origin/develop_KTG
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.conf import settings

# 프로젝트 내부 모듈
from .models import UserProfile, MainPhoto, SubPhoto


def generate_state():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

# 메인 홈 화면
def mainhome(request):
    return render(request, 'oreo/mainhome.html')

# 로그인 후 홈 화면
<<<<<<< HEAD
# @login_required 데코레이터 제거
=======
@login_required
>>>>>>> origin/develop_KTG
def loginhome_view(request):
    """
    로그인 후 메인 홈 화면을 보여주는 뷰
    - 사용자의 프로필 정보 표시
    - 사용자의 메인/서브 사진들 표시
    """
<<<<<<< HEAD
    # 세션 체크
    if request.session.get('is_authenticated'):
        user_email = request.session.get('user_email')
        try:
            user_profile = UserProfile.objects.get(email=user_email)
            main_photos = MainPhoto.objects.filter(user_profile=user_profile)
            
            photo_data = []
            for photo in main_photos:
                sub_photos = [sub.file.url for sub in photo.sub_photos.all()]
                photo_data.append({
                    'id': photo.id,  # ID 추가
                    'main_photo': photo.file.url,
                    'text': photo.text,
                    'date': photo.date,  # 날짜 정보 추가
                    'sub_photos': sub_photos,
                })
            
            return render(request, 'oreo/loginhome.html', {
                'photo_data': photo_data,
                'nickname': user_profile.nickname
            })
        except UserProfile.DoesNotExist:
            return redirect('login')
    return redirect('login')

    

# @login_required
# def loginhome(request):
#     try:
#         user_profile = UserProfile.objects.get(email=request.session.get('user_email'))
#         main_photos = MainPhoto.objects.filter(user_profile=user_profile)
        
#         photos_data = []
#         for main_photo in main_photos:
#             sub_photos = SubPhoto.objects.filter(main_photo=main_photo)
#             sub_photos_data = [{
#                 'url': sub_photo.file.url,
#                 'date': sub_photo.date.strftime('%Y-%m-%d') if sub_photo.date else None,
#                 'text': sub_photo.text
#             } for sub_photo in sub_photos]
            
#             photos_data.append({
#                 'main_photo': main_photo.file.url,
#                 'date': main_photo.date.strftime('%Y-%m-%d') if main_photo.date else None,
#                 'text': main_photo.text,
#                 'sub_photos': sub_photos_data
#             })

#         return render(request, 'oreo/loginhome.html', {'photos_data': photos_data})
#     except UserProfile.DoesNotExist:
#         return redirect('login')
=======
    try:
        # 세션에서 이메일 가져오기
        user_email = request.session.get('user_email')
        
        # UserProfile 가져오기
        user_profile = UserProfile.objects.get(email=user_email)
        nickname = user_profile.nickname
        
        # MainPhoto와 연결된 SubPhoto 가져오기
        main_photos = MainPhoto.objects.filter(user_profile=user_profile)
        
        # 데이터 구조화
        photo_data = []
        for main_photo in main_photos:
            sub_photos = SubPhoto.objects.filter(main_photo=main_photo)
            photo_data.append({
                "main_photo": main_photo.file.url,
                "description": main_photo.text,
                "date": main_photo.date,
                "sub_photos": [sub.file.url for sub in sub_photos]
            })

        context = {
            'nickname': nickname,
            'photo_data': photo_data,
        }
        
        return render(request, 'oreo/loginhome.html', context)
        
    except UserProfile.DoesNotExist:
        logger.error("UserProfile does not exist for the email.")
        return JsonResponse({'error': '사용자 프로필을 찾을 수 없습니다.'}, status=404)
    except Exception as e:
        logger.error(f"Error in loginhome_view: {str(e)}")
        return JsonResponse({'error': '페이지를 불러오는데 실패했습니다.'}, status=500)
    

    

def login_home(request):
    user_profile = request.user.userprofile  # 로그인한 사용자 프로필 가져오기
    
    main_photos = MainPhoto.objects.filter(user_profile=user_profile)  # 메인 사진 조회

    # 서브 사진을 각 메인 사진에 연결
    photo_data = []
    for main_photo in main_photos:
        sub_photos = SubPhoto.objects.filter(main_photo=main_photo)
        photo_data.append({
            "main_photo": main_photo.file.url,
            "description": main_photo.text,
            "date": main_photo.date,
            "sub_photos": [sub.file.url for sub in sub_photos]
        })

    context = {
        'photo_data': photo_data,  # 조회된 데이터를 템플릿으로 전달
    }
    return render(request, 'oreo/loginhome.html', context)
>>>>>>> origin/develop_KTG


# 로그인 페이지
def login_view(request):
    return render(request, 'oreo/login.html')

import logging  # 파일 상단에 추가

# 로거 설정
logger = logging.getLogger(__name__)

<<<<<<< HEAD
# 로그인
@csrf_exempt
def login_data(request):
    if request.method == 'POST':
        try:
            # POST 데이터 직접 접근
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            logger.info(f"Login attempt - Email: {email}")
            logger.info(f"Request POST data: {request.POST}")
            
            if not email or not password:
                return JsonResponse({
                    'error': '이메일과 비밀번호를 모두 입력해주세요.'
                }, status=400)

            # UserProfile 확인
            user_profile = UserProfile.objects.get(email=email)
            
            # 비밀번호 검증
            if check_password(password, user_profile.password):
                # 세션 설정
                request.session['user_email'] = email
                request.session['user_nickname'] = user_profile.nickname
                request.session['is_authenticated'] = True
                request.session.save()
                
                logger.info(f"Login successful - Email: {email}")
                logger.info(f"Session data: {dict(request.session)}")
                
                return JsonResponse({
                    'success': True,
=======
def login_data(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        logger.info(f"Login attempt - Email: {email}")
        
        try:
            user_profile = UserProfile.objects.get(email=email)
            
            if user_profile.check_password(password):
                request.session['user_email'] = email
                request.session['user_nickname'] = user_profile.nickname
                logger.info(f"Login successful for email: {email}")
                return JsonResponse({
                    'success': True, 
>>>>>>> origin/develop_KTG
                    'redirect_url': '/loginhome/'
                })
            else:
                logger.warning(f"Password mismatch for email: {email}")
                return JsonResponse({
                    'error': '비밀번호가 일치하지 않습니다.'
                }, status=400)
                
        except UserProfile.DoesNotExist:
<<<<<<< HEAD
            logger.warning(f"UserProfile not found - Email: {email}")
            return JsonResponse({
                'error': '등록되지 않은 이메일입니다.'
            }, status=400)
        except Exception as e:
            logger.error(f"Login error: {str(e)}")
            return JsonResponse({
                'error': '로그인 처리 중 오류가 발생했습니다.'
            }, status=400)
    
    return JsonResponse({'error': '잘못된 요청입니다.'}, status=405)
    
=======
            logger.warning(f"No user found with email: {email}")
            return JsonResponse({
                'error': '등록되지 않은 이메일입니다.'
            }, status=400)
        
>>>>>>> origin/develop_KTG

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
    return render(request, 'oreo/idfind.html')

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
    return render(request, 'oreo/pwfind.html')

# 재설정
def resetpassword_view(request):
    return render(request, 'oreo/resetpassword.html')

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
    return JsonResponse({'error': '잘못된 요청입니다.'}, status=405)


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
    return render(request, 'oreo/signup.html')

# 회원가입 단계 2 페이지
def signup1_view(request):
    return render(request, 'oreo/signup1.html')

# 파일 업로드 페이지
<<<<<<< HEAD
# @login_required 데코레이터 제거
def uplode_view(request):
    """
    파일 업로드 페이지를 보여주는 뷰
    - 세션 기반 인증 확인
    - 인증되지 않은 경우 로그인 페이지로 리다이렉트
    """
    # 세션 체크
    if not request.session.get('is_authenticated'):
        return redirect('login')
    
    # 인증된 사용자의 이메일 가져오기
    user_email = request.session.get('user_email')
    
    try:
        user_profile = UserProfile.objects.get(email=user_email)
        context = {
            'nickname': user_profile.nickname,
            'is_authenticated': True
        }
        return render(request, 'oreo/uplode.html', context)
    except UserProfile.DoesNotExist:
        # 세션은 있지만 사용자 프로필이 없는 경우
        return redirect('login')
    except Exception as e:
        logger.error(f"Error in uplode_view: {str(e)}")
        return redirect('login')


@csrf_exempt
def uplode_photo(request):
    if request.method == 'POST':
        try:
            # 상세 로깅 추가
            logger.info("=== Upload Process Start ===")
            logger.info(f"Files in request: {request.FILES.keys()}")
            logger.info(f"RepFile: {request.FILES.get('repFile')}")
            logger.info(f"SubFiles: {request.FILES.getlist('files')}")
            logger.info(f"Date: {request.POST.get('date')}")
            logger.info(f"Description: {request.POST.get('description')}")

            # 사용자 확인
            user_email = request.session.get('user_email')
            logger.info(f"User email from session: {user_email}")
            
            if not user_email:
                return JsonResponse({"error": "로그인이 필요합니다."}, status=401)

            try:
                user_profile = UserProfile.objects.get(email=user_email)
                logger.info(f"Found user profile: {user_profile.email}")
            except UserProfile.DoesNotExist:
                logger.error(f"UserProfile not found for email: {user_email}")
                return JsonResponse({"error": "사용자 프로필을 찾을 수 없습니다."}, status=400)

            # 파일 데이터 확인
            rep_file = request.FILES.get('repFile')
            if not rep_file:
                return JsonResponse({"error": "대표 사진이 필요합니다."}, status=400)

            upload_date = request.POST.get('date')
            description = request.POST.get('description', '')

            try:
                # MainPhoto 저장
                logger.info("Creating MainPhoto...")
                main_photo = MainPhoto.objects.create(
                    user_profile=user_profile,
                    file=rep_file,
                    text=description
                )
                # date 필드 따로 설정
                main_photo.date = upload_date
                main_photo.save()
                
                logger.info(f"MainPhoto created: {main_photo.id}")

                # SubPhotos 저장
                sub_photos_data = []
                for file in request.FILES.getlist('files'):
                    logger.info(f"Processing sub photo: {file.name}")
                    sub_photo = SubPhoto.objects.create(
                        main_photo=main_photo,
                        file=file,
                        text=description
                    )
                    # date 필드 따로 설정
                    sub_photo.date = upload_date
                    sub_photo.save()
                    
                    sub_photos_data.append({
                        'url': sub_photo.file.url,
                        'date': upload_date,
                        'text': description
                    })
                    logger.info(f"SubPhoto created: {sub_photo.id}")

                response_data = {
                    "success": True,
                    "message": "업로드 성공!",
                    "main_photo": {
                        "url": main_photo.file.url,
                        "date": upload_date,
                        "text": description
                    },
                    "sub_photos": sub_photos_data
                }
                logger.info("=== Upload Process Complete ===")
                return JsonResponse(response_data)

            except Exception as e:
                logger.error(f"Error during photo creation: {str(e)}")
                if main_photo:
                    main_photo.delete()  # 롤백
                return JsonResponse({"error": f"사진 저장 중 오류: {str(e)}"}, status=400)

        except Exception as e:
            logger.error(f"General upload error: {str(e)}")
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "잘못된 요청입니다."}, status=400)
=======
def uplode_view(request):
    return render(request, 'oreo/uplode.html')


@login_required
def uplode_photo(request):
    if request.method == 'POST':
        user_profile = request.user  # UserProfile 객체를 직접 사용

        # 데이터 가져오기
        rep_file = request.FILES.get('repFile')
        sub_files = request.FILES.getlist('files')
        date = request.POST.get('date')
        description = request.POST.get('description')

        if not rep_file or not date or not description:
            return JsonResponse({"message": "모든 필드가 필요합니다."}, status=400)
        
        # MainPhoto 저장
        main_photo = MainPhoto.objects.create(
            user_profile=user_profile,  # user_profile 직접 사용
            file=rep_file,
            text=description,
            date=date
        )

        # SubPhotos 저장
        for file in sub_files:
            SubPhoto.objects.create(
                main_photo=main_photo,
                file=file
            )

        return JsonResponse({"message": "업로드 성공!"}, status=201)
    return JsonResponse({"message": "잘못된 요청입니다."}, status=400)
>>>>>>> origin/develop_KTG

# 사진 데이터 가져오기
def album_data(request):
    if request.user.is_authenticated:
        try:
            # User에 해당하는 사진 목록을 가져옵니다.
            photos = MainPhoto.objects.filter(user_profile=request.user.userprofile)
            
            # 필요한 형식으로 데이터 가공
            data = [{
                'date': photo.date.strftime('%Y-%m-%d'),  # 날짜 형식 변경 (예: '2024-12-06')
                'file': photo.file.url,  # 파일 URL (media 경로)
                'text': photo.description or '',  # text가 null인 경우 빈 문자열로 처리
            } for photo in photos]
            
            # JSON 형식으로 응답
            return JsonResponse(data, safe=False)
        except Exception as e:
            return JsonResponse({'message': f'서버 오류: {str(e)}'}, status=500)
    else:
        return JsonResponse({'message': '로그인 상태가   닙니다.'}, status=401)


# 예시: 현재 로그인한 사용자에 해당하는 사진만 조회
<<<<<<< HEAD
def get_user_photos(request):
    if not request.session.get('is_authenticated'):
        return JsonResponse({'error': '로그인이 필요합니다.'}, status=401)
    
    user_email = request.session.get('user_email')
    try:
        user_profile = UserProfile.objects.get(email=user_email)
        main_photos = MainPhoto.objects.filter(user_profile=user_profile)
        sub_photos = SubPhoto.objects.filter(main_photo__user_profile=user_profile)
        
        # main_photos와 sub_photos에 대한 데이터를 반환
        main_photos_data = []
        for photo in main_photos:
            main_photos_data.append({
                "file_url": photo.file.url,
                "text": photo.text,
                "date": photo.date.strftime('%Y-%m-%d') if photo.date else None,  # 날짜 형식화
                "description": photo.description
            })

        sub_photos_data = []
        for sub_photo in sub_photos:
            sub_photos_data.append({
                "file_url": sub_photo.file.url,
                "text": sub_photo.text,
                "date": photo.date.strftime('%Y-%m-%d') if photo.date else None,  # 날짜 형식화
                "description": photo.description
            })

        return JsonResponse({
            "main_photos": main_photos_data, 
            "sub_photos": sub_photos_data
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
=======
@login_required
def get_user_photos(request):
    user_profile = request.user.userprofile  # 현재 사용자의 UserProfile을 가져옴
    main_photos = MainPhoto.objects.filter(user_profile=user_profile)  # 해당 사용자의 MainPhoto 조회
    sub_photos = SubPhoto.objects.filter(main_photo__user_profile=user_profile)  # 해당 사용자의 SubPhoto 조회
    
    # main_photos와 sub_photos에 대한 데이터를 반환
    main_photos_data = []
    for photo in main_photos:
        main_photos_data.append({
            "file_url": photo.file.url,
            "thumbnail_url": photo.thumbnail_url(),  # 썸네일 URL 추가
            "text": photo.text,
            "date": photo.date,
            "description": photo.description
        })

    sub_photos_data = []
    for sub_photo in sub_photos:
        sub_photos_data.append({
            "file_url": sub_photo.file.url,
            "text": sub_photo.text,
        })

    return JsonResponse({
        "main_photos": main_photos_data, 
        "sub_photos": sub_photos_data
    })
>>>>>>> origin/develop_KTG



# 사진 삭제
<<<<<<< HEAD
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import MainPhoto, SubPhoto
import json

@csrf_exempt
def delete_photo(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            photo_ids = data.get('photoIds', [])

            if not photo_ids:
                return JsonResponse({'error': '삭제할 사진 ID가 필요합니다.'}, status=400)

            # 현재 로그인한 사용자 확인
            user_email = request.session.get('user_email')
            if not user_email:
                return JsonResponse({'error': '로그인이 필요합니다.'}, status=401)

            try:
                user_profile = UserProfile.objects.get(email=user_email)
            except UserProfile.DoesNotExist:
                return JsonResponse({'error': '사용자를 찾을 수 없습니다.'}, status=404)

            deleted_count = 0
            for photo_id in photo_ids:
                try:
                    # 사용자의 메인 사진인지 확인
                    main_photo = MainPhoto.objects.get(
                        id=photo_id,
                        user_profile=user_profile
                    )

                    # 관련된 서브 사진들 삭제
                    # SubPhoto 모델의 delete() 메서드가 파일도 함께 삭제
                    sub_photos = main_photo.sub_photos.all()
                    for sub_photo in sub_photos:
                        sub_photo.delete()

                    # 메인 사진 삭제
                    # MainPhoto 모델의 delete() 메서드가 파일도 함께 삭제
                    main_photo.delete()
                    deleted_count += 1

                except MainPhoto.DoesNotExist:
                    return JsonResponse({
                        'error': f'ID {photo_id}에 해당하는 사진을 찾을 수 없습니다.'
                    }, status=404)

            return JsonResponse({
                'success': True,
                'message': f'{deleted_count}개의 사진이 삭제되었습니다.'
            })

        except json.JSONDecodeError:
            return JsonResponse({'error': '잘못된 데이터 형식입니다.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': '잘못된 요청입니다.'}, status=405)
=======
def delete_photo(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        album_index = data.get('albumIndex')
        photo_index = data.get('photoIndex')

        # 앨범 및 사진 삭제 로직 작성
        # 예: 데이터베이스에서 특정 사진 삭제
        success = True  # 성공 여부

        if success:
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False}, status=400)
>>>>>>> origin/develop_KTG
        
# QR 스캔 페이지
def qrscan_view(request):
    return render(request, 'oreo/qrscan.html')

# 로그아웃 처리
def logout_view(request):
    logout(request)
    return redirect('mainhome')


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

            logger.info(f"Registration attempt - Email: {email}")
            logger.info(f"Original password: {password}")

            if not all([email, password, real_name]):
                return JsonResponse({'error': '모든 필드를 입력해야 합니다.'}, status=400)

            # 비밀번호 해시화
            hashed_password = make_password(password)
            logger.info(f"Hashed password during registration: {hashed_password}")

<<<<<<< HEAD
            # UserProfile 생성
            user_profile = UserProfile.objects.create(
                email=email,
                password=hashed_password,
                real_name=real_name
=======
            # 사용자 생성
            user_profile = UserProfile.objects.create(
                email=email,
                password=hashed_password,  # 해시화된 비밀번호 저장
                real_name=real_name,
>>>>>>> origin/develop_KTG
            )
            
            logger.info(f"User created successfully with email: {email}")
            return JsonResponse({
                'message': '회원가입 1단계 완료', 
                'email': user_profile.email
            }, status=201)

        except Exception as e:
            logger.error(f"Registration error: {str(e)}")
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


@csrf_exempt
def register_user(request):
    """
    회원가입: 이메일, 비밀번호, 닉네임 입력받아 사용자 생성.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')
            nickname = data.get('nickname')

            # 사용자 생성
            user = UserProfile.objects.create(
                email_id=email,
                password=make_password(password),
                nickname=nickname
            )
            return JsonResponse({'message': 'User registered successfully', 'user_id': user.id}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


def kakao_login(request):
    state = generate_state()
    request.session['kakao_state'] = state  # 세션에 저장
    kakao_auth_url = (
        f"{settings.KAKAO_AUTH_URL}?response_type=code&"
        f"client_id={settings.KAKAO_REST_API_KEY}&"
        f"redirect_uri={settings.KAKAO_REDIRECT_URI}&"
        f"state={state}"
    )
    print("Generated Kakao Auth URL:", kakao_auth_url)  # 디버깅용 출력
    return redirect(kakao_auth_url)

def kakao_callback(request):
    # 카카오에서 리디렉션된 인증 코드 받기
    code = request.GET.get('code')
    if not code:
        return render(request, 'error.html', {'message': 'No code parameter found'})

    # 카카오 토큰 발급 요청 URL
    token_url = "https://kauth.kakao.com/oauth/token"
    client_id = settings.KAKAO_REST_API_KEY
    redirect_uri = settings.KAKAO_REDIRECT_URI

    # 요청 데이터
    data = {
        'grant_type': 'authorization_code',
        'client_id': client_id,
        'redirect_uri': redirect_uri,
        'code': code,
        'client_secret': settings.KAKAO_CLIENT_SECRET,
    }

    try:
        # 액세스 토큰 요청
        response = requests.post(token_url, data=data)
        if response.status_code == 200:
            token_data = response.json()
            access_token = token_data.get('access_token')

            # 사용자 정보 요청
            user_info_url = "https://kapi.kakao.com/v2/user/me"
            headers = {'Authorization': f'Bearer {access_token}'}
            user_info_response = requests.get(user_info_url, headers=headers)

            if user_info_response.status_code == 200:
                user_data = user_info_response.json()
                kakao_id = user_data['id']
                nickname = user_data['properties'].get('nickname', '')

                # UserProfile 저장 또는 업데이트
                user, created = UserProfile.objects.get_or_create(
                    kakao_id=kakao_id,
                    defaults={'nickname': nickname}
                )

                # 세션에 사용자 이름 저장
                request.session['user_nickname'] = nickname
                return redirect('loginhome')  # 로그인 성공 후 loginhome으로 리다이렉트
            else:
                return render(request, 'error.html', {'message': 'Failed to get user info from Kakao'})
        else:
            return render(request, 'error.html', {'message': 'Failed to get access token from Kakao'})

    except Exception as e:
        return render(request, 'error.html', {'message': f'An error occurred: {str(e)}'})

def is_logged_in(request):
    return 'user_email' in request.session

# QR URL 저장 API
@csrf_exempt
def save_qr_url(request, user_id):
    """
    사용자 URL 저장.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            url = data.get('url')

            validator = URLValidator()
            try:
                validator(url)
            except ValidationError:
                return JsonResponse({'error': 'Invalid URL'}, status=400)

            user = UserProfile.objects.get(id=user_id)
            user.urls.append(url)
            user.save()

            return JsonResponse({'message': 'URL saved successfully', 'user_id': user.id}, status=201)
        except UserProfile.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)