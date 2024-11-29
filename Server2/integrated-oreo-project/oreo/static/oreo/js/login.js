document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('loginForm');

    // 로그인 폼 제출 시 처리
    loginForm.addEventListener('submit', function (event) {
        event.preventDefault(); // 기본 폼 제출 방지

        // 아이디와 비밀번호 값 가져오기
        const Email = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        // CSRF 토큰 가져오기
        const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

        // 실제 요청 처리
        fetch('/login/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken, // CSRF 토큰 추가
            },
            body: JSON.stringify({ email: Email, password: password })
        })
            .then((response) => {
                if (response.ok) {
                    // 로그인 성공 시 LoginHome 페이지로 이동
                    window.location.href = '/LoginHome/';
                } else {
                    // 로그인 실패 시 오류 메시지 표시
                    return response.json().then((data) => {
                        alert(data.error || '아이디 또는 비밀번호가 일치하지 않습니다.');
                    });
                }
            })
            .catch((error) => {
                console.error('오류 발생:', error);
                alert('로그인 중 오류가 발생했습니다. 다시 시도하세요.');
            });
    });

    // 회원가입 링크 클릭 시 회원가입 페이지로 이동
    document.getElementById("signupLink").addEventListener("click", function () {
        const signupUrl = this.getAttribute("data-url");
        window.location.href = signupUrl;
    });

    // 아이디 찾기 링크 클릭 시 아이디 찾기 페이지로 이동
    document.getElementById("findIdBtn").addEventListener("click", function () {
        const idfindUrl = this.getAttribute("data-url");
        window.location.href = idfindUrl;
    });

    // 비밀번호 찾기 링크 클릭 시 비밀번호 찾기 페이지로 이동
    document.getElementById("findPwBtn").addEventListener("click", function () {
        const pwfindUrl = this.getAttribute("data-url");
        window.location.href = pwfindUrl;
    });
});
