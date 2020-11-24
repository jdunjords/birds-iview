import numpy as np
import sys
import tensorflow as tf
import cv2
from tensorflow import keras
from tensorflow.keras.models import load_model

# get the image, and process it into format that keras expects
img_path = sys.argv[1]
img = cv2.imread(img_path)
img = cv2.resize(img, (224,224))
img = np.expand_dims(img, axis=0)

model = load_model('models/3birds.h5')

print(model.predict(img))

