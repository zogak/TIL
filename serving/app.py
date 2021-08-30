import os
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

import numpy as np
from keras.models import load_model
from keras.preprocessing import image
from PIL import Image

app = Flask(__name__)

model = load_model('fashion-mnist.h5')
labels = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(28,28))

    img = img.convert('L')
    pixel = image.img_to_array(img)
    pixel = np.expand_dims(pixel, axis=0)

    preds = model.predict(pixel)
    return preds

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method=='POST':
        f = request.files['file']

        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        preds = model_predict(file_path, model)
        pred = np.argmax(preds)
        res = labels[pred]

        return str(res)
    
    return 'error'

if __name__ == '__main__':
    app.run(debug=True)