from flask import Flask, render_template, request, jsonify, redirect, url_for
from keras.models import load_model
from PIL import Image
from io import BytesIO
import base64
import numpy as np

app = Flask(__name__)
model = load_model("C:\\Users\\Samikshya\\Documents\\starting fresh(csv approach)\\25epochs.h5")

# Your existing class_indices dictionary
class_indices = {
    0: 'क', 1: 'ख', 2: 'ग', 3: 'घ', 4: 'ङ', 5: 'च', 6: 'छ', 7: 'ज', 8: 'झ', 9: 'ञ',
    10: 'ट', 11: 'ठ', 12: 'ड', 13: 'ढ', 14: 'ण', 15: 'त', 16: 'थ', 17: 'द', 18: 'ध',
    19: 'न', 20: 'प', 21: 'फ', 22: 'ब', 23: 'भ', 24: 'म', 25: 'य', 26: 'र', 27: 'ल',
    28: 'व', 29: 'श', 30: 'ष', 31: 'स', 32: 'ह', 33: 'क्ष', 34: 'त्र', 35: 'ज्ञ',
    36: '०', 37: '१', 38: '२', 39: '३', 40: '४', 41: '५', 42: '६', 43: '७', 44: '८', 45: '९'
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict')
def predict_page():
    return render_template('predict.html')

# Route for upload page
@app.route('/upload')
def upload_page():
    return render_template('upload.html')

@app.route('/word')
def word_page():
    return render_template('word.html')

@app.route('/predict', methods=['POST'])
def predict_character():
    # Get the image data from the canvas
    img_data = request.form['img_data'].split(",")[1]
    img = Image.open(BytesIO(base64.b64decode(img_data)))

    # Resize to your model's input size
    img = img.resize((32, 32))

    # Convert to grayscale and normalize
    img_array = np.array(img.convert("L")) / 255.0

    # Make prediction
    input_image = np.expand_dims(np.expand_dims(img_array, axis=0), axis=3)
    predicted_probs = model.predict(input_image)
    predicted_label_index = np.argmax(predicted_probs)

    # Get the predicted label name from the class_indices dictionary
    predicted_label_name = class_indices.get(predicted_label_index, "Unknown Class")

    # Get the probability of the predicted class
    probability = float(predicted_probs[0][predicted_label_index])

    return jsonify({'prediction': predicted_label_name, 'probability': probability})

@app.route('/uploadimg', methods=['POST'])
def predict_image():
    # Get the image data from the form
    img_data = request.form['img_data']
    img = Image.open(BytesIO(base64.b64decode(img_data)))

    # Resize to your model's input size
    img = img.resize((32, 32))

    # Convert to grayscale and normalize
    img_array = np.array(img.convert("L")) / 255.0

    # Make prediction
    input_image = np.expand_dims(np.expand_dims(img_array, axis=0), axis=3)
    predicted_probs = model.predict(input_image)
    predicted_label_index = np.argmax(predicted_probs)

    # Get the predicted label name from the class_indices dictionary
    predicted_label_name = class_indices.get(predicted_label_index, "Unknown Class")

    # Get the probability of the predicted class
    probability = float(predicted_probs[0][predicted_label_index])

    return jsonify({'prediction': predicted_label_name, 'probability': probability})


# Redirect from '/' to the home page
@app.route('/home')
def redirect_to_home():
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)