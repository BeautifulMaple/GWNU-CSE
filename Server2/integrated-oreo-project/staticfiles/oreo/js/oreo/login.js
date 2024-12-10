document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('loginForm');

    loginForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const formData = new FormData(this);
        
        fetch('/login_data/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
            body: formData
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