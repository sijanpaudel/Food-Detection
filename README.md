# Food Detection Web App

This web app uses your device's camera to capture an image, sends it to a Flask backend, and predicts the type of food using a pre-trained deep learning model.

## Features
- Capture food images using your device's camera
- Predict the food type using a Flask backend
- Display the prediction result

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/sijanpaudel/Food-Detection.git
   cd food-detection-web-app

2. Install backend dependencies:

    ```bash
    pip install -r requirements.txt

3. Run the Flask server:

    ```bash
    flask run

4. Open index.html in your browser to access the web app.

## Usage
Start the Flask backend at http://127.0.0.1:5000/.
Open the web app at http://127.0.0.1:5500/ and capture an image.
The food prediction will be displayed on the screen.