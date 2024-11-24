let verificationCode = ''; // To store generated verification code

// 뒤로가기 버튼 클릭 시 URL 이동
document.getElementById("backBtn").addEventListener("click", function() {
    const backUrl = this.getAttribute("data-url");
    if (backUrl) {
        window.location.href = backUrl; // data-url 값으로 리디렉션
    } else {
        history.back(); // 이전 페이지로 이동
    }
});

// 인증번호 받기 버튼 클릭 시
document.getElementById("verificationBtn").addEventListener("click", function() {
    const name = document.getElementById("name").value.trim();
    const phone = document.getElementById("phone").value.trim();

    if (!name || !phone) {
        alert("이름과 전화번호를 입력해 주세요.");
        return;
    }

    if (!/^\d{10,11}$/.test(phone)) {
        alert("알맞은 전화번호를 입력해주세요.");
        return;
    }

    // 6자리 인증번호 생성
    verificationCode = Math.floor(100000 + Math.random() * 900000).toString();
    alert("인증번호가 발급되었습니다: " + verificationCode);

    // 인증번호 입력 및 확인 버튼 활성화
    document.getElementById("verificationCode").disabled = false;
    document.getElementById("confirmCodeBtn").disabled = false;
});

// 인증번호 확인 버튼 클릭 시
document.getElementById("confirmCodeBtn").addEventListener("click", function() {
    const enteredCode = document.getElementById("verificationCode").value.trim();

    if (enteredCode !== verificationCode) {
        alert("인증번호가 다릅니다.");
    } else {
        alert("인증번호가 확인되었습니다.");
        // 아이디 찾기 버튼 활성화
        document.getElementById("findIdBtn").disabled = false;
    }
});

// 아이디 찾기 버튼 클릭 시
document.getElementById("findIdBtn").addEventListener("click", function() {
    const userId = "example_user"; // 실제 사용자 아이디를 찾는 로직으로 대체해야 함
    alert("당신의 아이디는 " + userId + "입니다.");

    // 로그인 페이지로 이동
    const loginUrl = this.getAttribute("data-url");
    if (loginUrl) {
        window.location.href = loginUrl; // data-url 값으로 리디렉션
    } else {
        alert("로그인 페이지 URL이 설정되지 않았습니다.");
    }
});
