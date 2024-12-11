document.addEventListener('DOMContentLoaded', function () {
    const albumGallery = document.getElementById('albumGallery');
    const storyGallery = document.getElementById('storyGallery');

    // 앨범에서 메인 사진 클릭 시 처리
    albumGallery.addEventListener('click', function (event) {
        const clickedPhoto = event.target;

        // 클릭한 요소가 메인 사진인지 확인
        if (clickedPhoto.classList.contains('main-photo')) {
            const photoElement = clickedPhoto.closest('.photo'); // 클릭된 사진의 부모 요소

            // 데이터 가져오기
            const description = photoElement.dataset.description;
            const date = photoElement.dataset.date;
            const subPhotos = photoElement.dataset.subPhotos ? photoElement.dataset.subPhotos.split(',') : [];

            // 스토리 섹션 갱신
            updateStoryGallery(clickedPhoto.src, description, date, subPhotos);
        }
    });

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
