document.getElementById("completeSignupBtn").addEventListener("click", async function () {
    const nicknameInput = document.getElementById("nickname");
    const nickname = nicknameInput.value.trim();

    // user_id는 회원가입 1단계에서 받은 값을 세션 저장소에서 가져온다고 가정
    const userId = sessionStorage.getItem('user_id');

    if (!nickname) {
        alert("닉네임을 입력하셔야 가능합니다.");
        nicknameInput.focus();
        return;
    }

    if (!userId) {
        alert("회원가입 정보를 찾을 수 없습니다. 처음부터 다시 시도해주세요.");
        return;
    }

    try {
        const response = await fetch('/register_user/step2/', { // URL 확인
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken') // CSRF 토큰 처리
            },
            body: JSON.stringify({ user_id: userId, nickname }) // JSON 형식으로 데이터 전송
        });

        if (response.ok) {
            const data = await response.json();
            alert("회원가입이 완료되었습니다!");
            window.location.href = this.dataset.url; // data-url에 저장된 login.html로 이동
        } else {
            const error = await response.json();
            alert(error.error || "오류가 발생했습니다. 다시 시도해주세요.");
        }
    } catch (err) {
        console.error(err);
        alert("네트워크 오류가 발생했습니다.");
    }
});
console.log(getCookie('csrftoken'));


// CSRF 토큰 처리 함수
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}
