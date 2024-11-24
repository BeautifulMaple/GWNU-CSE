document.addEventListener('DOMContentLoaded', () => {
    const uploadForm = document.getElementById('uploadForm');
    const backBtn = document.getElementById('backBtn');

    // 업로드 폼 제출 이벤트
    uploadForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const date = document.getElementById('dateInput').value;
        const files = document.getElementById('fileInput').files;
        const repFile = document.getElementById('repFileInput').files[0];

        if (!date || !files.length || !repFile) {
            alert("모든 필드를 입력하세요.");
            return;
        }

        const formData = new FormData();
        formData.append('date', date);
        for (const file of files) {
            formData.append('files', file);
        }
        formData.append('repFile', repFile);

        // 서버로 데이터 전송 (예: Ajax 요청)
        // 실제 구현 시 아래에 서버로 데이터 업로드 로직 추가
        console.log("업로드 데이터:", {
            date,
            files: Array.from(files).map(file => file.name),
            repFile: repFile.name
        });

        // 업로드 완료 알림 및 LoginHome 페이지로 이동
        alert("업로드가 완료되었습니다.");
        window.location.href = 'LoginHome.html';
    });

    // 뒤로가기 버튼 클릭 이벤트
    backBtn.addEventListener('click', (event) => {
        event.preventDefault(); // 기본 동작 방지
        window.location.href = 'LoginHome.html'; // LoginHome 페이지로 이동
    });
});
