document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('loginForm');

    loginForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        // FormData 대신 JSON 데이터로 전송
        fetch('/login_data/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
            body: JSON.stringify({
                email: email,
                password: password
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                window.location.href = data.redirect_url;
            } else {
                alert(data.error || '로그인에 실패했습니다.');
            }
        })
        .catch(error => {
            console.error('오류 발생:', error);
            alert('로그인 중 오류가 발생했습니다.');
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