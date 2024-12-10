// CSRF 토큰 가져오는 함수
function getCsrfToken() {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]');
    return csrfToken ? csrfToken.value : '';
}

// 회원가입 1단계에서 사용자 정보를 서버에 POST 요청 후
async function registerUserStep1() {
    const passwordInput = document.getElementById('password');
    const emailInput = document.getElementById('email');
    const realNameInput = document.getElementById('name');

    const password = passwordInput.value.trim();
    const email = emailInput.value.trim();
    const realName = realNameInput.value.trim();

    if (!email || !password || !realName) {
        alert('모든 필드를 입력해주세요.');
        return;
    }

    try {
        const response = await fetch('/register_user/step1/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCsrfToken(),
            },
            body: JSON.stringify({ email: email, password, real_name: realName }),
        });

        if (response.ok) {
            const data = await response.json();
            sessionStorage.setItem('email', data.email); // email를 sessionStorage에 저장
            alert('1단계 회원가입이 완료되었습니다.');
            // 다음 단계로 진행
        } else {
            const error = await response.json();
            alert(error.error || '회원가입 중 문제가 발생했습니다.');
        }
    } catch (err) {
        console.error(err);
        alert('네트워크 오류가 발생했습니다.');
    }
}

// 다음으로 버튼 클릭 이벤트
document.getElementById('nextBtn').addEventListener('click', registerUserStep1);


// email 중복 확인
document.getElementById('email').addEventListener('blur', function () {
    const email = this.value;

    if (!email) {
        alert('아이디를 입력해주세요.');
        return;
    }

    fetch('/register_user/step1/check_email/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCsrfToken(),
        },
        body: JSON.stringify({ email: email }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('서버 응답이 좋지 않습니다.');
        }
        return response.json();
    })
    .then(data => {
        if (data.is_duplicate) {
            alert('이미 사용 중인 아이디입니다.');
        } else {
            alert('사용 가능한 아이디입니다.');
        }
    })
    .catch(error => {
        console.error('에러 발생:', error);
        alert('아이디 확인 중 문제가 발생했습니다.');
    });
});

// 이메일 중복 확인 및 인증번호 발송
document.getElementById('sendCodeBtn').addEventListener('click', function () {
    const email = document.getElementById('email').value;

    if (!email) {
        alert('Email을 입력해주세요.');
        return;
    }

    fetch('/register_user/step1/check_email/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCsrfToken(),
        },
        body: JSON.stringify({ email: email }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('서버 응답이 좋지 않습니다.');
        }
        return response.json();
    })
    .then(data => {
        if (data.is_duplicate) {
            alert('이미 사용 중인 이메일입니다.');
        } else {
            alert('사용 가능한 이메일입니다. 인증번호를 발송합니다.');
            // 인증번호 발송 로직 추가
        }
    })
    .catch(error => {
        console.error('에러 발생:', error);
        alert('이메일 확인 중 문제가 발생했습니다.');
    });
});

// 인증번호 발송
document.getElementById('sendCodeBtn').addEventListener('click', function () {
    const email = document.getElementById('email').value;

    if (!email) {
        alert('Email을 입력해주세요.');
        return;
    }

    fetch('/register_user/step1/send_verification_code/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCsrfToken(),
        },
        body: JSON.stringify({ email: email }),  // JSON 형식으로 이메일 데이터 전송
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('서버 응답이 좋지 않습니다.');
        }
        return response.json();
    })
    .then(data => {
        alert(data.message); // 사용자에게 메시지 표시
    })
    .catch(error => {
        console.error('에러 발생:', error);
        alert('인증 코드 발송 중 문제가 발생했습니다.');
    });
});

// 다음으로 버튼 클릭 이벤트
document.getElementById('nextBtn').addEventListener('click', function () {
    const email = document.getElementById('email').value;
    const userCode = document.getElementById('verificationCode').value;

    if (!email || !userCode) {
        alert('Email과 인증번호를 입력해주세요.');
        return;
    }

    fetch('/register_user/step1/verify_code/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCsrfToken(),
        },
        body: JSON.stringify({ email: email, code: userCode }), // 이메일과 인증 코드를 전송
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('서버 응답이 좋지 않습니다.');
            }
            return response.json();
        })
        .then(data => {
            if (data.is_valid) {
                alert('인증이 완료되었습니다.');
                // 페이지 이동
                window.location.href = document.getElementById('nextBtn').dataset.url;
            } else {
                alert('인증 코드가 일치하지 않습니다.');
            }
        })
        .catch(error => {
            console.error('에러 발생:', error);
            alert('인증 확인 중 문제가 발생했습니다.');
        });
});
