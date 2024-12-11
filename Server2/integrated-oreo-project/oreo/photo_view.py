from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import MainPhoto, SubPhoto, UserProfile
from .serializers import MainPhotoSerializer, SubPhotoSerializer


class MainPhotoView(APIView):
    """
    MainPhoto와 SubPhoto 업로드 및 CRUD API
    """
    def post(self, request):
        rep_photo = request.FILES.get('rep_photo')  # 대표 사진
        sub_photos = request.FILES.getlist('sub_photos')  # 서브 사진/동영상
        date = request.data.get('date')
        description = request.data.get('description')

        if not (rep_photo and date and description):
            return Response({'success': False, 'message': '필수 데이터가 누락되었습니다.'}, status=status.HTTP_400_BAD_REQUEST)

        user = request.user  # 로그인한 사용자 정보
        main_photo = MainPhoto.objects.create(
            user_profile=user,
            file=rep_photo,
            text=description,
            date=date
        )

        # 서브 사진/동영상 저장
        for sub_file in sub_photos:
            SubPhoto.objects.create(
                main_photo=main_photo,
                file=sub_file,
                text='',  # 추가 설명은 비워둠
            )

        return Response({'success': True, 'message': '업로드 성공!', 'main_photo_id': main_photo.id}, status=status.HTTP_201_CREATED)

    """
    SubPhoto에 대한 CRUD API
    """
    def post(self, request, pk=None):
        if pk:  # MainPhoto를 찾아서 연결하는 방식
            main_photo = get_object_or_404(MainPhoto, pk=pk)
            data = request.data.copy()
            data['main_photo'] = main_photo.id
            serializer = SubPhotoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        if pk:  # 특정 서브사진을 조회
            sub_photo = get_object_or_404(SubPhoto, pk=pk)
            serializer = SubPhotoSerializer(sub_photo)
            return Response(serializer.data)

    def delete(self, request, pk):
        sub_photo = get_object_or_404(SubPhoto, pk=pk)
        sub_photo.delete()
        return Response({'message': 'Sub photo deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class SubPhotoView(APIView):
    """
    SubPhoto에 대한 CRUD API
    """
    def post(self, request, pk=None):
        if pk:  # MainPhoto를 찾아서 연결하는 방식
            main_photo = get_object_or_404(MainPhoto, pk=pk)
            data = request.data.copy()
            data['main_photo'] = main_photo.id
            serializer = SubPhotoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        if pk:  # 특정 서브사진을 조회
            sub_photo = get_object_or_404(SubPhoto, pk=pk)
            serializer = SubPhotoSerializer(sub_photo)
            return Response(serializer.data)

    def delete(self, request, pk):
        sub_photo = get_object_or_404(SubPhoto, pk=pk)
        sub_photo.delete()
        return Response({'message': 'Sub photo deleted successfully'}, status=status.HTTP_204_NO_CONTENT)