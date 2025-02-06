from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from predict import transform_image, get_prediction
from PIL import Image

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
CLASS_NAMES = ['apple_pie', 'bread_pudding', 'breakfast_burrito', 'carrot_cake', 'cheese_plate', 'cheesecake', 'chicken_curry', 'chicken_wings', 'chocolate_cake', 'chocolate_mousse', 'cup_cakes', 'donuts', 'dumplings', 'fish_and_chips', 'french_fries', 'french_onion_soup', 'french_toast', 'fried_rice', 'frozen_yogurt', 'garlic_bread', 'greek_salad', 'grilled_cheese_sandwich', 'hamburger', 'hot_dog', 'ice_cream', 'omelette', 'pancakes', 'pizza', 'ramen', 'samosa', 'sashimi', 'steak', 'sushi']

def allowed_file(filename):
    ### xxx.png
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/predict", methods=["POST"])
def predict():

    if request.method == "POST":
        file = request.files.get("file")
        if file is None or file.filename == "":
            return jsonify({'error': 'no file'})
        if not allowed_file(file.filename):
            return jsonify({'error': 'format not supported'})
        
        try:
            img_bytes = file.read()
            tensor = transform_image(img_bytes)
            prediction = get_prediction(tensor)
            data = {'prediction': prediction.item(), 'class_name':CLASS_NAMES[prediction.item()]}
            return jsonify(data)
        except:
            return jsonify({'error': 'error during prediction'})