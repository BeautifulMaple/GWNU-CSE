let verificationCode = ''; // To store generated verification code

// Event listener for 뒤로가기 (Back) button
document.getElementById("backBtn").addEventListener("click", function() {
    window.location.href = "login.html";
});

// Event listener for 인증번호 받기 (Get Verification Code)
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

    // Generate a random 6-digit verification code
    verificationCode = Math.floor(100000 + Math.random() * 900000).toString();
    alert("인증번호가 발급되었습니다: " + verificationCode);

    // Enable verification input and confirm button
    document.getElementById("verificationCode").disabled = false;
    document.getElementById("confirmCodeBtn").disabled = false;
});

// Event listener for 확인 (Confirm Code)
document.getElementById("confirmCodeBtn").addEventListener("click", function() {
    const enteredCode = document.getElementById("verificationCode").value.trim();

    if (enteredCode !== verificationCode) {
        alert("인증번호가 다릅니다.");
    } else {
        alert("인증번호가 확인되었습니다.");
        // Proceed to allow user to find their ID
        document.getElementById("findIdBtn").disabled = false;
    }
});

// Event listener for 아이디 찾기 (Find ID)
document.getElementById("findIdBtn").addEventListener("click", function() {
    // Here we should implement logic to find the user's ID (e.g., from a database)
    const userId = "example_user"; // This should be replaced with real data
    alert("당신의 아이디는 " + userId + "입니다.");
    window.location.href = "login.html"; // Redirect back to the login page
});
