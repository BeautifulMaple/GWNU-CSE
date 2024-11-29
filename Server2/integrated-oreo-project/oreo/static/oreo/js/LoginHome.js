document.addEventListener('DOMContentLoaded', () => {
    const albumGallery = document.getElementById('albumGallery');
    const storyGallery = document.getElementById('storyGallery');

    // 예시 데이터
    const albums = [
        {
            date: '2024.11.18',
            thumbnail: 'https://via.placeholder.com/100x100?text=Album1',
            photos: [
                'https://via.placeholder.com/100x100?text=Photo1',
                'https://via.placeholder.com/100x100?text=Photo2',
                'https://via.placeholder.com/100x100?text=Photo3',
            ],
        },
        {
            date: '2024.11.19',
            thumbnail: 'https://via.placeholder.com/100x100?text=Album2',
            photos: [
                'https://via.placeholder.com/100x100?text=Photo4',
                'https://via.placeholder.com/100x100?text=Photo5',
                'https://via.placeholder.com/100x100?text=Photo6',
            ],
        },
    ];

    // My Album 섹션에 대표 사진 추가
    albums.forEach((album) => {
        const albumItem = document.createElement('div');
        albumItem.classList.add('album-item');

        const img = document.createElement('img');
        img.src = album.thumbnail;
        img.alt = `${album.date} 대표 사진`;
        img.classList.add('album-thumbnail');

        const dateLabel = document.createElement('span');
        dateLabel.textContent = album.date;
        dateLabel.classList.add('album-date');

        albumItem.appendChild(img);
        albumItem.appendChild(dateLabel);

        // 대표 사진 클릭 이벤트
        albumItem.addEventListener('click', () => {
            updateStoryGallery(album.date, album.photos);
        });

        albumGallery.appendChild(albumItem);
    });

    // My Story 섹션 갤러리 업데이트
    function updateStoryGallery(date, photos) {
        storyGallery.innerHTML = `<h3>${date}</h3>`;
        photos.forEach((photo) => {
            const img = document.createElement('img');
            img.src = photo;
            img.alt = `${date} 사진`;
            img.classList.add('story-photo');
            storyGallery.appendChild(img);
        });
    }
});

document.addEventListener('DOMContentLoaded', () => {
    const logoutBtn = document.getElementById('logoutBtn');
    const uploadBtn = document.getElementById('uploadBtn');
    const qrScanBtn = document.getElementById('qrScanBtn');

    // 로그아웃 버튼 이벤트
    logoutBtn.addEventListener('click', function () {
        if (confirm('로그아웃하시겠습니까?')) {
            window.location.href = '/logout/'; // Django 로그아웃 URL 호출
        }
    });

    // 업로드 버튼 이벤트
    uploadBtn.addEventListener('click', function () {
        window.location.href = '/uplode'; // 업로드 페이지로 이동
    });

    // QR 스캔 버튼 이벤트
    qrScanBtn.addEventListener('click', function () {
        window.location.href = '/QRscan'; // QR 스캔 페이지로 이동
    });
});
