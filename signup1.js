document.getElementById("completeSignupBtn").addEventListener("click", function() {
    const nickname = document.getElementById("nickname").value.trim();

    if (nickname === "") {
        alert("닉네임을 입력하셔야 가능합니다.");
    } else {
        // 닉네임이 입력되었으면 login.html로 이동
        window.location.href = "login.html";
    }
});
