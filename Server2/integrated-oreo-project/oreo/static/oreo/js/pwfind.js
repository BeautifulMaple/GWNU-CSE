// CSRF 토큰 가져오는 함수
function getCsrfToken() {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]');
    return csrfToken ? csrfToken.value : '';
}

// 인증번호 발송
document.getElementById('verificationBtn').addEventListener('click', async function () {
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();

    if (!name || !email) {
        alert('이름과 이메일을 입력해주세요.');
        return;
    }

    try {
        const response = await fetch('/register_user/step1/send_verification_code/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCsrfToken(),
            },
            body: JSON.stringify({ email: email }), // 이메일 데이터 전송
        });

        if (response.ok) {
            const data = await response.json();
            alert(data.message); // 사용자에게 메시지 표시
            document.getElementById('verificationCode').disabled = false; // 인증번호 입력 활성화
            document.getElementById('confirmCodeBtn').disabled = false; // 확인 버튼 활성화
        } else {
            const error = await response.json();
            alert(error.error || '인증번호 발송 중 문제가 발생했습니다.');
        }
    } catch (error) {
        console.error('에러 발생:', error);
        alert('네트워크 오류가 발생했습니다.');
    }
});

// 인증번호 확인
document.getElementById('confirmCodeBtn').addEventListener('click', async function () {
    const email = document.getElementById('email').value.trim();
    const verificationCode = document.getElementById('verificationCode').value.trim();

    if (!verificationCode) {
        alert('인증번호를 입력해주세요.');
        return;
    }

    try {
        const response = await fetch('/register_user/step1/verify_code/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCsrfToken(),
            },
            body: JSON.stringify({ email: email, code: verificationCode }), // 이메일과 인증 코드를 전송
        });

        if (response.ok) {
            const data = await response.json();
            if (data.is_valid) {
                alert('인증이 완료되었습니다.');
                document.getElementById('findIdBtn').disabled = false; // 다음 버튼 활성화
            } else {
                alert('인증 코드가 일치하지 않습니다.');
            }
        } else {
            const error = await response.json();
            alert(error.error || '인증 확인 중 문제가 발생했습니다.');
        }
    } catch (error) {
        console.error('에러 발생:', error);
        alert('네트워크 오류가 발생했습니다.');
    }
});

// 비밀번호 찾기 - resetpassword 페이지로 이동
document.getElementById('findIdBtn').addEventListener('click', function () {
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const verificationCode = document.getElementById('verificationCode').value.trim();

    if (!name || !email || !verificationCode) {
        alert('이름, 이메일, 인증번호를 입력해주세요.');
        return;
    }

    // 리다이렉션
    const resetPasswordUrl = this.dataset.url;
    window.location.href = resetPasswordUrl;
});

// 뒤로가기 버튼 클릭 이벤트
document.getElementById('backBtn').addEventListener('click', function () {
    window.location.href = this.dataset.url; // 로그인 페이지로 이동
});
