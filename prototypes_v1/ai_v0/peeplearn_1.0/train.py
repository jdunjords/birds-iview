import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense, Flatten, BatchNormalization, Conv2D, MaxPool2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import confusion_matrix
import os
import itertools
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


train_path = '3birds/train'
valid_path = '3birds/valid'
test_path = '3birds/test'

train_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input).flow_from_directory(directory=train_path, target_size=(224,224), classes=['Purple_Finch', 'Blue_Jay', 'Red_headed_Woodpecker'], batch_size=10)

valid_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input).flow_from_directory(directory=valid_path, target_size=(224,224), classes=['Purple_Finch', 'Blue_Jay', 'Red_headed_Woodpecker'], batch_size=10)

test_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input).flow_from_directory(directory=test_path, target_size=(224,224), classes=['Purple_Finch', 'Blue_Jay', 'Red_headed_Woodpecker'], batch_size=10, shuffle=False)

assert train_batches.n == 150 
assert valid_batches.n == 15
assert test_batches.n == 15

imgs, labels = next(train_batches)

'''
# Sanity check
def plotImages(images_arr):
        fig, axes = plt.subplots(1,10,figsize=(20,20))
        axes = axes.flatten()
        for img, ax in zip(images_arr,axes):
                ax.imshow(img)
                ax.axis('off')
        plt.tight_layout()
        plt.show()

plotImages(imgs)
print(labels)
'''

model = Sequential([
Conv2D(filters=32, kernel_size=(3,3), activation='relu', padding='same', input_shape=(224,224,3)),
MaxPool2D(pool_size=(2,2), strides=2),
Conv2D(filters=64, kernel_size=(3,3), activation='relu', padding='same'),
MaxPool2D(pool_size=(2,2), strides=2),
Flatten(),
Dense(units=3, activation='softmax')
])

model.compile(optimizer=Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x=train_batches, validation_data=valid_batches, epochs=5, verbose=2)
model.summary()
model.save('models/3birds.h5')
