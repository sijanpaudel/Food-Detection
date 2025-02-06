const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const captureButton = document.getElementById('capture');
const photo = document.getElementById('photo');
const result = document.getElementById('result');

// 1️ Access the Camera
navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream;
    })
    .catch(err => {
        console.error("Error accessing camera: ", err);
        result.innerText = "Error accessing camera. Please ensure you have granted permission.";
    });

// Ensure video metadata is loaded
video.addEventListener('loadedmetadata', () => {
    video.width = video.videoWidth;
    video.height = video.videoHeight;
});

// 2️ Capture and Send Image

captureButton.addEventListener("click", async () => {
    const context = canvas.getContext("2d");
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    context.drawImage(video, 0, 0, canvas.width, canvas.height);

    // Convert canvas image to Blob
    canvas.toBlob(async (blob) => {
        if (!blob) {
            console.error("Blob conversion failed!");
            result.innerText = "Error capturing image.";
            return;
        }

        const formData = new FormData();
        formData.append("file", blob, "food.png"); // Correct field name!

        try {
            const response = await fetch("http://127.0.0.1:5000/predict", {
                method: "POST",
                body: formData
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            result.innerText = `Detected Food: ${data.class_name}`;
        } catch (error) {
            console.error("Error sending image:", error);
            result.innerText = "Error identifying food. Please try again.";
        }
    }, "image/png"); // Ensure image format is specified
});
