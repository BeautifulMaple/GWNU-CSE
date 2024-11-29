// CSRF 토큰 가져오기 함수
function getCsrfToken() {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]');
    return csrfToken ? csrfToken.value : '';
}

// 비밀번호 변경 버튼 이벤트
document.getElementById('resetPasswordBtn').addEventListener('click', async function () {
    const newPassword = document.getElementById('new_password').value.trim();
    const confirmPassword = document.getElementById('confirm_password').value.trim();

    // 입력값 검증
    if (!newPassword || !confirmPassword) {
        alert('비밀번호와 비밀번호 확인을 모두 입력해주세요.');
        return;
    }

    if (newPassword.length < 8) {
        alert('비밀번호는 최소 8자리 이상이어야 합니다.');
        return;
    }

    if (newPassword !== confirmPassword) {
        alert('비밀번호와 비밀번호 확인이 일치하지 않습니다.');
        return;
    }

    try {
        // 서버로 비밀번호 변경 요청 보내기
        const response = await fetch('/reset_password/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCsrfToken(),
            },
            body: JSON.stringify({ password: newPassword }), // 비밀번호 데이터 전송
        });

        if (response.ok) {
            const data = await response.json();
            alert(data.message || '비밀번호가 성공적으로 변경되었습니다.');
            window.location.href = document.getElementById('backToLoginBtn').dataset.url; // 로그인 페이지로 이동
        } else {
            const error = await response.json();
            alert(error.error || '비밀번호 변경 중 문제가 발생했습니다.');
        }
    } catch (error) {
        console.error('에러 발생:', error);
        alert('네트워크 오류가 발생했습니다.');
    }
});

// 로그인 페이지로 돌아가기 버튼 이벤트
document.getElementById('backToLoginBtn').addEventListener('click', function () {
    window.location.href = this.dataset.url; // 로그인 페이지로 이동
});
