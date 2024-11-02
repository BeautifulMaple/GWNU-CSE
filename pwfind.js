document.getElementById('sendCodeBtn').addEventListener('click', function() {
    // 6자리 랜덤 인증번호 생성
    let verificationCode = Math.floor(100000 + Math.random() * 900000);
    
    // 인증번호를 사용자에게 알림
    alert('인증번호가 발급되었습니다: ' + verificationCode);
    
    // 인증번호를 전역 변수로 저장
    window.verificationCode = verificationCode;
});

document.getElementById('verifyCodeBtn').addEventListener('click', function() {
    const enteredCode = document.getElementById('verificationCode').value;
    
    // 입력된 인증번호와 발급된 인증번호 비교
    if (enteredCode == window.verificationCode) {
        alert('인증번호가 확인되었습니다.');
    } else {
        alert('인증번호가 틀렸습니다.');
    }
});


// IDFind.html에서 뒤로가기 버튼을 클릭했을 때 login.html로 이동하는 함수
document.getElementById("backBtn").addEventListener("click", function() {
    window.location.href = "login.html";
});
