document.addEventListener("DOMContentLoaded", () => {
    const repFileInput = document.getElementById("repFileInput");
    const fileInput = document.getElementById("fileInput");
    const repPreview = document.getElementById("repPreview");
    const previewContainer = document.getElementById("previewContainer");
    const backBtn = document.getElementById("backBtn");

    // 대표 사진 미리보기 처리
    repFileInput.addEventListener("change", (event) => {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                repPreview.src = e.target.result;
                repPreview.classList.remove("hidden");
            };
            reader.readAsDataURL(file);
        } else {
            repPreview.src = ""; // 미리보기 초기화
            repPreview.classList.add("hidden");
        }
    });

    // 뒤로가기 버튼 클릭 처리
    backBtn.addEventListener("click", () => {
        const url = backBtn.getAttribute("data-url");
        window.location.href = url;
    });

    // 파일 업로드 처리
    const uplodeForm = document.getElementById("uplodeForm");
    uplodeForm.addEventListener("submit", async (event) => {
        event.preventDefault(); // 기본 제출 동작 방지

        // 입력값 가져오기
        const repFile = repFileInput.files[0];
        const files = fileInput.files;
        const date = document.getElementById("dateInput").value;
        const description = document.getElementById("descriptionInput").value;

        // 로그 출력 (폼 제출 시점)
        console.log("대표 사진:", repFile);
        console.log("파일 목록:", files);
        console.log("날짜:", date);
        console.log("설명:", description);

        // 필드 유효성 검증
        if (!repFile) {
            alert("대표 사진을 선택하세요.");
            return;
        }

        if (files.length === 0) {
            alert("최소 한 개의 파일을 선택하세요.");
            return;
        }

        if (!date) {
            alert("날짜를 입력하세요.");
            return;
        }

        if (!description.trim()) {
            alert("설명을 입력하세요.");
            return;
        }

        // 폼 데이터 생성
        const formData = new FormData();
        formData.append("repFile", repFile); // 서버에서 요구하는 대표 사진 필드 이름
        for (const file of files) {
            formData.append("files", file); // 다중 파일 업로드 처리
        }
        formData.append("date", date);
        formData.append("description", description);

        try {
            // 서버에 데이터 전송
            const response = await fetch(uplodeForm.action, {
                method: "POST",
                body: formData,
                headers: {
                    "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
                },
            });

            if (response.ok) {
                const albumData = await response.json();  // 서버에서 반환된 album-data 처리
                console.log("업로드 성공, 반환된 데이터:", albumData);
                alert("업로드 성공!");
                window.location.href = backBtn.getAttribute("data-url"); // LoginHome 페이지로 이동
            } else {
                const errorData = await response.json();
                console.error("서버 응답 오류:", errorData);
                alert(`업로드 실패: ${errorData.message || "서버 오류"}`);
            }
        } catch (error) {
            console.error("업로드 중 오류:", error);
            alert("업로드 중 오류가 발생했습니다. 다시 시도해주세요.");
        }
    });
});

// 로그인 상태 확인 (Django 템플릿 변수 사용)
const isAuthenticated = JSON.parse(document.getElementById("isAuthenticated").textContent);
if (!isAuthenticated) {
    alert("로그인 상태가 아닙니다. 로그인 후 시도하세요.");
    window.location.href = "/login/"; // 로그인 페이지로 이동
}
