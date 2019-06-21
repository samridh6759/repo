from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout,Conv2D,MaxPooling2D,Flatten,Activation
import numpy as np
import cv2
import os
import matplotlib.pyplot as plt
import random
import pickle
pick_in=open('X.pickle','rb')
X=pickle.load(pick_in)
pick_in=open('y.pickle','rb')
y=pickle.load(pick_in)
X=X/255.0
model=Sequential()
model.add(Conv2D(64,(3,3),input_shape=X.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(64,(3,3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(64,(3,3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(64))

model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss="binary_crossentropy",optimizer="Adam",metrics=['accuracy'])

model.fit(X,y,epochs=10,batch_size=32,validation_split=0.1)   # validation_split is the amount of data to be split after each epoch
model.save("CATS_DOGS_CNN.model")