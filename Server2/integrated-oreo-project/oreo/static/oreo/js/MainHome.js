document.addEventListener('DOMContentLoaded', () => {
    const albumGallery = document.getElementById('albumGallery');
    const storyGallery = document.getElementById('storyGallery');

    // 예시 데이터
    const albums = [
        {
            date: '2024.11.18',
            thumbnail: '/static/oreo/images/testimg/photo1_thumb.jpg',
            photos: [
                '/static/oreo/images/testimg/photo1_thumb.jpg',
                '/static/oreo/images/testimg/photo2_thumb.jpg',
            ],
        },
        {
            date: '2024.11.19',
            thumbnail: '/static/oreo/images/testimg/photo3_thumb.jpg',
            photos: [
                '/static/oreo/images/testimg/photo3_thumb.jpg',
                '/static/oreo/images/testimg/photo4_thumb.jpg',
            ],
        },
    ];

    if (albumGallery && storyGallery) {
        albums.forEach((album) => {
            const albumItem = document.createElement('div');
            albumItem.classList.add('album-item');

            const img = document.createElement('img');
            img.src = album.thumbnail;
            img.alt = `${album.date} 대표 사진`;
            img.classList.add('album-thumbnail');

            img.onerror = () => {
                img.src = '/static/oreo/images/default_thumb.jpg';
            };

            const dateLabel = document.createElement('span');
            dateLabel.textContent = album.date;
            dateLabel.classList.add('album-date');

            albumItem.appendChild(img);
            albumItem.appendChild(dateLabel);

            albumItem.addEventListener('click', () => {
                document.querySelectorAll('.album-item').forEach(item => item.classList.remove('selected'));
                albumItem.classList.add('selected');
                updateStoryGallery(album.date, album.photos);
            });

            albumGallery.appendChild(albumItem);
        });
    }

    function updateStoryGallery(date, photos) {
        storyGallery.innerHTML = `<h3>${date}</h3>`;
        photos.forEach((photo) => {
            const img = document.createElement('img');
            img.src = photo;
            img.alt = `${date} 사진`;
            img.classList.add('story-photo');

            img.onerror = () => {
                img.src = '/static/oreo/images/default_thumb.jpg';
            };

            storyGallery.appendChild(img);
        });
    }
});

document.addEventListener('DOMContentLoaded', () => {
    const loginBtn = document.getElementById('loginBtn');
    const uploadBtn = document.getElementById('uploadBtn');
    const qrScanBtn = document.getElementById('qrScanBtn');

    // 로그인 버튼 이벤트
    if (loginBtn) {
        loginBtn.addEventListener('click', (e) => {
            e.preventDefault(); // 기본 동작 차단
            console.log("로그인 버튼 클릭됨"); // 확인용 로그
            window.location.href = '/login'; // 로그인 페이지로 이동
        });
    }

    // 보호된 기능 처리 함수
    function handleProtectedAction(button, redirectUrl) {
        button.addEventListener('click', function (e) {
            e.preventDefault();
            const isLoggedIn = false; // 실제 로그인 상태를 확인하는 로직으로 대체해야 합니다

            if (!isLoggedIn) {
                const confirmLogin = confirm("이 기능은 로그인이 필요합니다. 로그인하시겠습니까?");
                if (confirmLogin) {
                    window.location.href = '/login'; // 로그인 페이지로 리디렉션
                }
            } else {
                window.location.href = redirectUrl; // 로그인 상태일 때 대상 페이지로 이동
            }
        });
    }

    if (uploadBtn) {
        handleProtectedAction(uploadBtn, '/uplode'); // 업로드 페이지로 이동
    }

    if (qrScanBtn) {
        handleProtectedAction(qrScanBtn, '/QRscan'); // QR 스캔 페이지로 이동
    }
});
