from flask import Flask, render_template, request
from preprocessor import preprocess_image
import numpy as np
import tensorflow as tf
import os
from PIL import Image

app = Flask(__name__, template_folder='templates')
model = tf.saved_model.load('./check')
test_path = 'static/test_img.jpg'


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/test', methods=['GET'])
def test():
    img = preprocess_image(test_path)
    prediction = model(img, training=False).numpy()
    prediction = np.squeeze(prediction)
    prediction = (prediction > 0.5).astype(np.uint8) * 255
    mask_path = os.path.join('static', 'uploads', 'prediction.png')
    mask_img = Image.fromarray(prediction)
    mask_img.save(mask_path)
    return render_template('result.html', mask_path=mask_path, original_img=test_path)



@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        original_img = request.files['image']
        original_img_path = os.path.join('static', 'uploads', 'original_img.png')
        original_img.save(original_img_path)
        img = preprocess_image(original_img_path)
        prediction = model(img, training=False).numpy()
        prediction = np.squeeze(prediction)
        prediction = (prediction > 0.5).astype(np.uint8) * 255
        mask_path = os.path.join('static', 'uploads', 'prediction.png')
        mask_img = Image.fromarray(prediction)
        mask_img.save(mask_path)
        return render_template('result.html', mask_path=mask_path, original_img=original_img_path)


if __name__ == '__main__':
    app.run(debug=True, port=5454)
