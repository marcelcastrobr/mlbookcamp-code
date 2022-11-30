

import tensorflow as tf
from tensorflow import keras


model = keras.models.load_model('clothing-model-v4.h5')

tf.saved_model.save(model, 'clothing-model')