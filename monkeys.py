# -*- coding: utf-8 -*-
"""monkeys.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Bb_rvJYJbrKcRHoTcgakn3dozSaYKhO_
"""

from keras.models import Sequential
import keras as k
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Conv2D, Activation, BatchNormalization, GlobalAvgPool2D, MaxPooling2D, Dropout

from keras import preprocessing

from google.colab import drive
drive.mount("/content/gdrive")

import zipfile
from google.colab import drive

drive.mount('/content/drive/')

zip_ref = zipfile.ZipFile("/content/monkeys.zip", 'r')
zip_ref.extractall()
zip_ref.close()

import tensorflow.keras as keras

file1= ('/content/training/training')

file2= ('/content/validation/validation')

from keras.preprocessing.image import ImageDataGenerator

train_datagen = k.preprocessing.image.ImageDataGenerator(rescale=1./255, horizontal_flip=True)

train_gen = train_datagen.flow_from_directory(directory = file1, subset='training', target_size=(150,150), shuffle=True, class_mode='categorical', batch_size=32)

val_gen = val_datagen.flow_from_directory(directory= file2, subset='validation', shuffle=True, class_mode='categorical', target_size=(150,150), batch_size=32)
val_datagen = k.preprocessing.image.ImageDataGenerator(rescale=1./255)

model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(150, 150, 3), strides=2))
model.add(Activation('relu'))

model.add(BatchNormalization())
model.add(Conv2D(32, (3, 3), strides=2))
model.add(Activation('relu'))

model.add(BatchNormalization())
model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(BatchNormalization())
model.add(Conv2D(64, (3, 3), strides=2))
model.add(Activation('relu'))

model.add(Conv2D(512, (1, 1), strides=2))
model.add(Activation('relu'))
model.add(Conv2D(10, (1, 1)))
model.add(GlobalAvgPool2D())
model.add(Activation('sigmoid'))

from tensorflow.keras.preprocessing.image import ImageDataGenerator

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])

model= model.fit(train_gen, validation_data = val_gen, epochs=25, verbose=2)

model.history['categorical_accuracy']

model.history['loss']

model.model.save('monkey_pred.h5')

import cv2

import matplotlib.pyplot as plt

import numpy as np


x = plt.imread('/white_headed_capuchin.jpg')
plt.imshow(x)

x = x/255

x = np.resize(x,(1,150,150,3))

x.shape

classes = list(train_gen.class_indices)

print(classes[np.argmax(model.model.predict(x))])