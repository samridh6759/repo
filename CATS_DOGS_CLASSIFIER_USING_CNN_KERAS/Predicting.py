from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout,Conv2D,MaxPooling2D,Flatten,Activation
import numpy as np
import cv2
import os
import matplotlib.pyplot as plt
import random
import pickle
def prepare(filepath):
    img_size=70
    img_array=cv2.imread(filepath,cv2.IMREAD_GRAYSCALE)
    new_array=cv2.resize(img_array,(img_size,img_size))
    return(new_array.reshape(-1,img_size,img_size,1))
model=tf.keras.models.load_model("CATS_DOGS_CNN.model")
inp=str(input('Image File name : '))
prediction=model.predict([prepare(inp)])
print(categories[int(prediction[0][0])])