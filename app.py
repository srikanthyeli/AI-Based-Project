from flask import Flask, render_template, request
import numpy as np
from PIL import Image
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))


def preprocess_image(image_file):
    image = Image.open(image_file).convert("RGB")
    image = image.resize((244, 244))
    image_array = np.array(image).astype(np.float32) / 255.0
    return np.expand_dims(image_array, axis=0)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return "No file uploaded"

    file = request.files['image']
    if file.filename == '':
        return "No file selected"

    img_array = preprocess_image(file)
    pred = model.predict(img_array)
    label = "cat" if pred[0][0] > 0.5 else "dog"
    confidence = round(float(pred[0][0]) if label == "cat" else 1 - float(pred[0][0]), 4)

    return render_template('result.html', label=label, confidence=confidence)

if __name__ == '__main__':
    app.run(debug=True)
