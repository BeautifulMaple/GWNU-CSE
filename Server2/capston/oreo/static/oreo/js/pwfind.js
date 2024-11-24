// 인증번호 요청 버튼 클릭 시
document.getElementById('sendCodeBtn').addEventListener('click', function() {
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();

    // 이름과 이메일 입력 확인
    if (!name || !email) {
        alert('이름과 이메일을 입력해주세요.');
        return;
    }

    // 이메일 형식 유효성 검사
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        alert('유효한 이메일 주소를 입력해주세요.');
        return;
    }

    // 6자리 랜덤 인증번호 생성
    let verificationCode = Math.floor(100000 + Math.random() * 900000);

    // 인증번호를 사용자에게 알림
    alert('인증번호가 발급되었습니다: ' + verificationCode);

    // 인증번호를 전역 변수로 저장
    window.verificationCode = verificationCode;

    // 인증번호 입력 필드 활성화
    document.getElementById('verificationCode').disabled = false;
});

// 인증번호 확인 버튼 클릭 시
document.getElementById('verifyCodeBtn').addEventListener('click', function() {
    const enteredCode = document.getElementById('verificationCode').value.trim();

    // 인증번호 입력 확인
    if (!enteredCode) {
        alert('인증번호를 입력해주세요.');
        return;
    }

    // 입력된 인증번호와 발급된 인증번호 비교
    if (enteredCode == window.verificationCode) {
        alert('인증번호가 확인되었습니다.');
        // 인증 성공 시 비밀번호 찾기 버튼 활성화
        document.getElementById('findPwdBtn').disabled = false;
    } else {
        alert('인증번호가 틀렸습니다.');
    }
});

// 비밀번호 찾기 버튼 클릭 시
document.getElementById('findPwdBtn').addEventListener('click', function(event) {
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const enteredCode = document.getElementById('verificationCode').value.trim();

    // 모든 필드 입력 확인
    if (!name || !email || !enteredCode) {
        alert('이름, 이메일, 인증번호를 모두 입력해주세요.');
        event.preventDefault(); // 폼 제출 방지
        return;
    }

    // 인증번호 유효성 확인
    if (enteredCode != window.verificationCode) {
        alert('유효하지 않은 인증번호입니다.');
        event.preventDefault(); // 폼 제출 방지
        return;
    }

    // 비밀번호 찾기 로직 수행
    alert('비밀번호 찾기 요청이 처리되었습니다.');

    // 로그인 페이지로 리디렉션
    window.location.href = '/login'; // 로그인 페이지 URL로 이동
});

// 뒤로가기 버튼 클릭 시 URL 이동
document.getElementById('backBtn').addEventListener('click', function() {
    const backUrl = this.getAttribute('data-url');
    if (backUrl) {
        window.location.href = backUrl; // data-url 값으로 리디렉션
    } else {
        history.back(); // 이전 페이지로 이동
    }
});
