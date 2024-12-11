document.addEventListener('DOMContentLoaded', () => {
    const thumbnailGallery = document.getElementById('thumbnailGallery');
    const photoGallery = document.getElementById('photoGallery');
    const photoInfoModal = document.getElementById('photoInfoModal');
    const photoInfo = document.getElementById('photoInfo');
    const closeModal = document.getElementById('closeModal');

    // 더미 데이터
    const data = [
        {
            date: '2024.03.01',
            thumbnail: 'images/testimg/photo3_thumb.jpg',
            photos: [
                { src: 'images/testimg/photo3_thumb.jpg', info: 'Photo 1 - 2024.03.01' },
                { src: 'images/data/2024.03.01/photo2.jpg', info: 'Photo 2 - 2024.03.01' }
            ]
        },
        {
            date: '2024.04.04',
            thumbnail: 'images/data/2024.04.04/rep2.jpg',
            photos: [
                { src: 'images/data/2024.04.04/photo3.jpg', info: 'Photo 3 - 2024.04.04' },
                { src: 'images/data/2024.04.04/photo4.jpg', info: 'Photo 4 - 2024.04.04' }
            ]
        }
    ];

    // 대표 사진 목록 생성
    data.forEach((album) => {
    const thumbnailItem = document.createElement('div');
    thumbnailItem.classList.add('thumbnail-item');

    // 이미지 요소 생성
    const img = document.createElement('img');
    img.src = album.thumbnail;
    img.classList.add('thumbnail-img');

    // 날짜 텍스트 생성
    const dateLabel = document.createElement('div');
    dateLabel.textContent = album.date;
    dateLabel.classList.add('thumbnail-date');

    // 이미지와 날짜 추가
    thumbnailItem.appendChild(img);
    thumbnailItem.appendChild(dateLabel);

    // 클릭 시 저장된 사진 목록 로드
    thumbnailItem.addEventListener('click', () => {
        loadPhotoGallery(album.photos);
    });

    thumbnailGallery.appendChild(thumbnailItem);
    });


    // 저장된 사진 목록 생성 함수
    function loadPhotoGallery(photos) {
        photoGallery.innerHTML = '';
        photos.forEach((photo) => {
            const img = document.createElement('img');
            img.src = photo.src;
            img.classList.add('photo-item');
            img.addEventListener('click', () => {
                showPhotoInfo(photo.info);
            });
            photoGallery.appendChild(img);
        });
    }

    // 사진 정보 모달 표시 함수
    function showPhotoInfo(info) {
        photoInfo.textContent = info;
        photoInfoModal.style.display = 'flex';
    }

    // 모달 닫기
    closeModal.addEventListener('click', () => {
        photoInfoModal.style.display = 'none';
    });
});
