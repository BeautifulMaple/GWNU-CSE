document.addEventListener('DOMContentLoaded', function () {
    const albumGallery = document.getElementById('albumGallery');
    const storyGallery = document.getElementById('storyGallery');
<<<<<<< HEAD
    const deleteButton = document.getElementById('deleteButton');
    const cancelButton = document.getElementById('cancelButton');
    const actionMenu = document.getElementById('actionMenu');
    let selectedPhotos = new Set();
=======
>>>>>>> origin/develop_KTG

    // 앨범에서 메인 사진 클릭 시 처리
    albumGallery.addEventListener('click', function (event) {
        const clickedPhoto = event.target;

<<<<<<< HEAD
        if (clickedPhoto.classList.contains('main-photo')) {
            const photoElement = clickedPhoto.closest('.photo');
=======
        // 클릭한 요소가 메인 사진인지 확인
        if (clickedPhoto.classList.contains('main-photo')) {
            const photoElement = clickedPhoto.closest('.photo'); // 클릭된 사진의 부모 요소

            // 데이터 가져오기
>>>>>>> origin/develop_KTG
            const description = photoElement.dataset.description;
            const date = photoElement.dataset.date;
            const subPhotos = photoElement.dataset.subPhotos ? photoElement.dataset.subPhotos.split(',') : [];

<<<<<<< HEAD
=======
            // 스토리 섹션 갱신
>>>>>>> origin/develop_KTG
            updateStoryGallery(clickedPhoto.src, description, date, subPhotos);
        }
    });

<<<<<<< HEAD
    albumGallery.addEventListener('mousedown', function(event) {
        const photoElement = event.target.closest('.photo');
        if (!photoElement) return;

        let pressTimer;
        pressTimer = setTimeout(function() {
            toggleSelection(photoElement);
        }, 1000);

        photoElement.addEventListener('mouseup', function() {
            clearTimeout(pressTimer);
        });

        photoElement.addEventListener('mouseleave', function() {
            clearTimeout(pressTimer);
        });
    });

    function toggleSelection(photoElement) {
        if (selectedPhotos.has(photoElement)) {
            selectedPhotos.delete(photoElement);
            photoElement.classList.remove('selected');
        } else {
            selectedPhotos.add(photoElement);
            photoElement.classList.add('selected');
        }
        updateActionMenuVisibility();
    }

    function updateActionMenuVisibility() {
        if (selectedPhotos.size > 0) {
            actionMenu.classList.remove('hidden');
        } else {
            actionMenu.classList.add('hidden');
        }
    }

    function updateStoryGallery(mainPhotoSrc, description, date, subPhotos) {
        storyGallery.innerHTML = '';

        const storyDiv = document.createElement('div');
        storyDiv.classList.add('story');

        const mainPhotoImg = document.createElement('img');
        mainPhotoImg.src = mainPhotoSrc;
        mainPhotoImg.classList.add('main-photo');

        const detailsDiv = document.createElement('div');
        detailsDiv.classList.add('story-details');

        const dateP = document.createElement('p');
        dateP.classList.add('story-date');
        if (date) {
            const formattedDate = new Date(date).toLocaleDateString('ko-KR', {
                year: 'numeric',
                month: 'long',
                day: 'numeric'
            });
            dateP.textContent = formattedDate;
        } else {
            dateP.textContent = '날짜 정보 없음';
        }

        const descriptionP = document.createElement('p');
        descriptionP.classList.add('story-description');
        descriptionP.textContent = description || '설명이 없습니다.';

        const subPhotosDiv = document.createElement('div');
        subPhotosDiv.classList.add('sub-photos-container');

        subPhotos.forEach(photoUrl => {
            const subPhotoImg = document.createElement('img');
            subPhotoImg.src = photoUrl;
            subPhotoImg.classList.add('sub-photo');
            subPhotoImg.addEventListener('click', function() {
                openModal(photoUrl);
            });
            subPhotosDiv.appendChild(subPhotoImg);
        });

        detailsDiv.appendChild(dateP);
        detailsDiv.appendChild(descriptionP);
        storyDiv.appendChild(mainPhotoImg);
        storyDiv.appendChild(detailsDiv);
        storyDiv.appendChild(subPhotosDiv);
        storyGallery.appendChild(storyDiv);
    }

    function openModal(photoUrl) {
        const modal = document.createElement('div');
        modal.classList.add('sub-photo-modal');

        const modalContent = document.createElement('img');
        modalContent.src = photoUrl;
        modalContent.classList.add('sub-photo-modal-content');

        const closeModal = document.createElement('span');
        closeModal.classList.add('close-modal');
        closeModal.innerHTML = '&times;';
        closeModal.onclick = function() {
            modal.style.display = 'none';
            modal.remove();
        };

        modal.appendChild(closeModal);
        modal.appendChild(modalContent);
        document.body.appendChild(modal);

        modal.style.display = 'block';
    }

    deleteButton.addEventListener('click', async function() {
        try {
            const photoIds = Array.from(selectedPhotos).map(photoElement => {
                return photoElement.dataset.id;
            });

            const response = await fetch('/delete_photo/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({ photoIds: photoIds })
            });

            if (response.ok) {
                const result = await response.json();
                alert('사진이 성공적으로 삭제되었습니다.');
                window.location.reload();
            } else {
                console.error('사진 삭제 실패');
                alert('사진 삭제에 실패했습니다.');
            }
        } catch (error) {
            console.error('오류 발생:', error);
            alert('오류가 발생했습니다.');
        }
    });

    cancelButton.addEventListener('click', function() {
        selectedPhotos.forEach(photoElement => {
            photoElement.classList.remove('selected');
        });
        
        selectedPhotos.clear();
        
        updateActionMenuVisibility();
    });

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
=======
    // 스토리 갤러리 업데이트 함수
    function updateStoryGallery(mainPhotoSrc, description, date, subPhotos) {
        // 스토리 갤러리 내용 초기화
        storyGallery.innerHTML = '';

        // 스토리 전체 컨테이너 생성
        const storyDiv = document.createElement('div');
        storyDiv.classList.add('story');

        // 메인 사진 추가
        const mainPhotoImg = document.createElement('img');
        mainPhotoImg.src = mainPhotoSrc;
        mainPhotoImg.alt = description;
        mainPhotoImg.classList.add('main-photo');

        // 날짜 및 설명 추가
        const storyDetailsBox = document.createElement('div');
        storyDetailsBox.classList.add('story-details-box');

        const dateParagraph = document.createElement('p');
        dateParagraph.classList.add('story-date');
        dateParagraph.textContent = date;

        const descriptionParagraph = document.createElement('p');
        descriptionParagraph.classList.add('story-description');
        descriptionParagraph.textContent = description;

        storyDetailsBox.appendChild(dateParagraph);
        storyDetailsBox.appendChild(descriptionParagraph);

        // 서브 사진 컨테이너 추가
        const subPhotoContainer = document.createElement('div');
        subPhotoContainer.classList.add('sub-photo-container');

        subPhotos.forEach((subPhotoSrc) => {
            const subPhotoImg = document.createElement('img');
            subPhotoImg.src = subPhotoSrc;
            subPhotoImg.alt = '서브 사진';
            subPhotoImg.classList.add('sub-photo');
            subPhotoContainer.appendChild(subPhotoImg);
        });

        // 요소 조합
        storyDiv.appendChild(mainPhotoImg);
        storyDiv.appendChild(storyDetailsBox);
        storyDiv.appendChild(subPhotoContainer);

        // 스토리 갤러리에 추가
        storyGallery.appendChild(storyDiv);
    }
});
>>>>>>> origin/develop_KTG
