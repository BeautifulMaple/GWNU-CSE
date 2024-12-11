document.addEventListener('DOMContentLoaded', () => {
    const startScanBtn = document.getElementById('startScanBtn');
    const scannerBox = document.getElementById('scannerBox');
    const backBtn = document.getElementById('backBtn');

    startScanBtn.addEventListener('click', async function() {
        if (await checkAndRequestCameraPermission()) {
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: "environment" } });
                startScanBtn.style.display = 'none';
                scannerBox.style.display = 'block';
                startCamera(stream);
            } catch (err) {
                console.error("카메라 접근에 실패했습니다: ", err);
                showCameraInstructions();
            }
        }
    });

    backBtn.addEventListener('click', function() {
        window.history.back();
    });
});

async function checkAndRequestCameraPermission() {
    if (navigator.permissions && navigator.permissions.query) {
        try {
            const result = await navigator.permissions.query({ name: 'camera' });
            if (result.state === 'granted') {
                return true;
            } else if (result.state === 'prompt') {
                return confirm("QR 코드 스캔을 위해 카메라를 사용합니다. 동의하시겠습니까?");
            } else if (result.state === 'denied') {
                showCameraInstructions();
                return false;
            }
        } catch (err) {
            console.error("권한 확인 오류:", err);
        }
    }
    
    // 권한 확인이 불가능한 경우 사용자에게 직접 물어봅니다.
    return confirm("QR 코드 스캔을 위해 카메라를 사용합니다. 동의하시겠습니까?");
}

function showCameraInstructions() {
    const instructions = `
        카메라 접근이 거부되었습니다. 브라우저 설정에서 카메라 권한을 허용해주세요.
        
        Android:
        1. 브라우저 설정으로 이동
        2. 사이트 설정 > 카메라 선택
        3. 이 사이트에 대해 '허용'으로 설정
        
        iOS:
        1. 설정 앱 열기
        2. Safari(또는 사용 중인 브라우저) 선택
        3. 카메라 접근 허용
        
        설정 변경 후 페이지를 새로고침 해주세요.
    `;
    alert(instructions);
}

function startCamera(stream) {
    const video = document.createElement('video');
    video.srcObject = stream;
    video.setAttribute('playsinline', true);
    video.play();

    const scannerBox = document.getElementById('scannerBox');
    scannerBox.innerHTML = '';
    scannerBox.appendChild(video);

    video.addEventListener('loadeddata', function() {
        scanQRCode(video, stream);
    });
}

function scanQRCode(video, stream) {
    const canvas = document.createElement('canvas');
    const context = canvas.getContext('2d');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    function scan() {
        context.drawImage(video, 0, 0, canvas.width, canvas.height);
        const imageData = context.getImageData(0, 0, canvas.width, canvas.height);
        const qrCode = jsQR(imageData.data, canvas.width, canvas.height);

        if (qrCode) {
            const qrData = qrCode.data;
            if (qrData.startsWith("http://") || qrData.startsWith("https://")) {
                // URL일 경우 사용자에게 이동할지 확인
                const confirmMove = confirm("해당 URL로 이동하시겠습니까?");
                if (confirmMove) {
                    window.location.href = qrData; // 확인을 누르면 URL로 이동
                }
            } else {
                alert("QR 코드가 스캔되었습니다: " + qrData); // URL이 아닌 경우 데이터만 표시
            }
            stopCamera(stream); // 카메라 종료
        } else {
            requestAnimationFrame(scan);
        }
    }
    scan();
}



function stopCamera(stream) {
    const tracks = stream.getTracks();
    tracks.forEach(track => track.stop());
    document.getElementById('scannerBox').style.display = 'none';
    document.getElementById('startScanBtn').style.display = 'block';
}