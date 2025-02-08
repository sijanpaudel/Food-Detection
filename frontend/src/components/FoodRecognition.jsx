import { useRef, useState, useEffect } from "react";
import "./FoodRecognition.css";


const FoodRecognition = () => {
    const videoRef = useRef(null);
    const canvasRef = useRef(null);
    const [photo, setPhoto] = useState(null);
    const [result, setResult] = useState("");

    useEffect(() => {
        // Access the camera
        navigator.mediaDevices.getUserMedia({ video: true })
            .then(stream => {
                if (videoRef.current) {
                    videoRef.current.srcObject = stream;
                }
            })
            .catch(err => {
                console.error("Error accessing camera: ", err);
                setResult("Error accessing camera. Please ensure you have granted permission.");
            });
    }, []);

    const captureImage = async () => {
        const video = videoRef.current;
        const canvas = canvasRef.current;
        if (!video || !canvas) return;

        const context = canvas.getContext("2d");
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        context.drawImage(video, 0, 0, canvas.width, canvas.height);

        canvas.toBlob(async (blob) => {
            if (!blob) {
                console.error("Blob conversion failed!");
                setResult("Error capturing image.");
                return;
            }

            const formData = new FormData();
            formData.append("file", blob, "food.png");

            try {
                const response = await fetch("http://127.0.0.1:5000/predict", {
                    method: "POST",
                    body: formData
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }

                const data = await response.json();
                setPhoto(URL.createObjectURL(blob));
                setResult(`Detected Food: ${data.class_name}`);
            } catch (error) {
                console.error("Error sending image:", error);
                setResult("Error identifying food. Please try again.");
            }
        }, "image/png");
    };

    return (
        <div className="container">
            <h2>Capture Food Image</h2>
            <video ref={videoRef} autoPlay></video>
            <button onClick={captureImage}>Capture</button>
            <canvas ref={canvasRef} style={{ display: "none" }}></canvas>
            {photo && <img src={photo} alt="Captured" />}
            <p>{result}</p>
        </div>
    );
};

export default FoodRecognition;
