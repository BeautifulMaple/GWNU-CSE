// 사진 버튼 클릭 시 동작
document.getElementById('photoBtn').addEventListener('click', function() {
    alert("사진 버튼이 클릭되었습니다.");
    // 여기에 사진 관련 동작을 추가하세요
});

// 동영상 버튼 클릭 시 동작
document.getElementById('videoBtn').addEventListener('click', function() {
    alert("동영상 버튼이 클릭되었습니다.");
    // 여기에 동영상 관련 동작을 추가하세요
});

// 뒤로가기 버튼 클릭 시 동작
document.getElementById('backBtn').addEventListener('click', function() {
    window.history.back(); // 이전 페이지로 이동
});
