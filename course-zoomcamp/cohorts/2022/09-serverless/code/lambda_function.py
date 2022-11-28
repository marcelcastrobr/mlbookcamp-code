#!/usr/bin/env python
# coding: utf-8
from io import BytesIO
from urllib import request
from PIL import Image
import tflite_runtime.interpreter as tflite
from keras_image_helper import create_preprocessor
import numpy as np

def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img

def prepare_input(x):
    return x / 255.0

preprocessor = create_preprocessor('xception', target_size=(150, 150))
interpreter = tflite.Interpreter(model_path='dino-vs-dragon-v2.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

def predict(url):
    image = download_image(url)
    target_size=(150, 150)
    image_prep = prepare_image(image,target_size)
    x = np.array(image_prep, dtype='float32')
    X = np.array([x])
    X = prepare_input(X)

    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)
    print(f'My predictions are: {preds}')
    float_predictions = preds[0].tolist()

    return float_predictions


def lambda_handler(event, context):
    url = event['url']
    result = predict(url)
    return result

