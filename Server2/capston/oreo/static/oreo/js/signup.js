document.getElementById('sendCodeBtn').addEventListener('click', function() {
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;

    if (email && phone) {
        alert('인증번호가 발송되었습니다.');
        // 실제 인증번호 발송 로직 추가 (예: 이메일 또는 SMS 발송)
    } else {
        alert('Email과 휴대폰번호를 입력해주세요.');
    }
});

document.getElementById('signupForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;

    if (password === confirmPassword) {
        alert('회원가입이 완료되었습니다.');
        // 실제 회원가입 로직 추가
    } else {
        alert('비밀번호가 일치하지 않습니다.');
    }
});

document.getElementById('nextBtn').addEventListener('click', function() {
    const signup1Url = this.getAttribute("data-url");
    if (signup1Url)
    {
    window.location.href = signup1Url; // signup1.html로 이동
    } else{
        alert('URL를 찾을 수 없습니다.');
    }
});
