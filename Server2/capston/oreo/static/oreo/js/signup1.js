document.getElementById("completeSignupBtn").addEventListener("click", async function () {
    const nicknameInput = document.getElementById("nickname");
    const nickname = nicknameInput.value.trim();

    if (!nickname) {
        alert("닉네임을 입력하셔야 가능합니다.");
        nicknameInput.focus();
        return;
    }

    try {
        const response = await fetch('/api/signup/nickname/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken') // CSRF 토큰 처리
            },
            body: JSON.stringify({ nickname })
        });

        if (response.ok) {
            const loginUrl = this.dataset.url;
            alert("회원가입이 완료되었습니다!");
            window.location.href = loginUrl;
        } else {
            const error = await response.json();
            alert(error.message || "오류가 발생했습니다. 다시 시도해주세요.");
        }
    } catch (err) {
        console.error(err);
        alert("네트워크 오류가 발생했습니다.");
    }
});

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}
