# Food Detection Web App

This web app uses your device's camera to capture an image, sends it to a Flask backend, and predicts the type of food using a pre-trained deep learning model.

## Features

- Capture food images using your device's camera  
- Predict the food type using a Flask backend  
- Display the prediction result in the React UI  

## Setup

### 1. Clone the Repository:
```sh
git clone https://github.com/sijanpaudel/Food-Detection.git
cd food-detection-web-app
```
### 2. Install Backend Dependencies
```sh
pip install -r requirements.txt
```

### 3. Run the Flask Server:
```sh
flask run
```

### 4. Install Frontend Dependencies:
```sh
cd frontend  # Navigate to the React app directory
npm install
```

### 5. Run the React App:
```sh
npm run dev
```
The React app will open at http://localhost:5173/ by default.

## Usage
1. Start the Flask backend at http://127.0.0.1:5000/.
2. Open the React web app (http://localhost:5173/).
3. Capture an image using your camera.
4. The food prediction result will be displayed on the screen.
