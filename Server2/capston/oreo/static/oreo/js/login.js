document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('loginForm');
    const loginBtn = document.getElementById('loginBtn');

    // 로그인 폼 제출 시 처리
    loginForm.addEventListener('submit', function (event) {
        event.preventDefault(); // 기본 폼 제출 방지

        // 이메일과 비밀번호 값 가져오기
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        
        // CSRF 토큰 가져오기
        const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

        // 이메일과 비밀번호 출력 (테스트용)
        console.log(`Email: ${email}, Password: ${password}`);

        // 실제 요청 처리
        fetch('/LoginHome', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken, // CSRF 토큰 추가
            },
            body: JSON.stringify({ email, password })
        })
            .then((response) => {
                if (response.ok) {
                    window.location.href = '/LoginHome';  // 성공 시 LoginHome 페이지로 이동
                } else {
                    alert('로그인 실패. 다시 시도하세요.');
                }
            })
            .catch((error) => {
                console.error('오류 발생:', error);
            });
    });

    // 회원가입 링크 클릭 시 회원가입 페이지로 이동
    document.getElementById("signupLink").addEventListener("click", function() {
        const signupUrl = this.getAttribute("data-url");
        window.location.href = signupUrl;
    });

    // 아이디 찾기 링크 클릭 시 아이디 찾기 페이지로 이동
    document.getElementById("findIdBtn").addEventListener("click", function() {
        const idfindUrl = this.getAttribute("data-url");
        window.location.href = idfindUrl;
    });

    // 비밀번호 찾기 링크 클릭 시 비밀번호 찾기 페이지로 이동
    document.getElementById("findPwBtn").addEventListener("click", function() {
        const pwfindUrl = this.getAttribute("data-url");
        window.location.href = pwfindUrl;
    });
});
