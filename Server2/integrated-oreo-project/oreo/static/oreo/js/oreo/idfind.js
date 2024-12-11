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
            body: JSON.stringify({ email: email }),  // 이메일 데이터 전송
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
                document.getElementById('findIdBtn').disabled = false; // 아이디 찾기 버튼 활성화
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

// 아이디 찾기
document.getElementById('findIdBtn').addEventListener('click', async function () {
    const name = document.getElementById('name').value.trim(); // 이름
    const email = document.getElementById('email').value.trim(); // 이메일
    const verificationCode = document.getElementById('verificationCode').value.trim(); // 인증 코드

    if (!name || !email || !verificationCode) { // 모든 필드 확인
        alert('이름, 이메일, 인증번호를 입력해주세요.');
        return;
    }

    try {
        const response = await fetch('/register_user/step1/find_id/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCsrfToken(),
            },
            body: JSON.stringify({ name: name, email: email, code: verificationCode }), // 모든 데이터 전송
        });

        if (response.ok) {
            const data = await response.json();
            alert(`당신의 아이디는: ${data.email}`); // 사용자 아이디 표시
        } else {
            const error = await response.json();
            alert(error.error || '아이디 찾기 중 문제가 발생했습니다.');
        }
    } catch (error) {
        console.error('에러 발생:', error);
        alert('네트워크 오류가 발생했습니다.');
    }
});



// 뒤로가기 버튼 클릭 이벤트
document.getElementById('backBtn').addEventListener('click', function () {
    window.location.href = this.dataset.url; // 로그인 페이지로 이동
});
