from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout,Conv2D,MaxPooling2D,Flatten,Activation
import numpy as np
import cv2
import os
import matplotlib.pyplot as plt
import random
import pickle
datadir= "C:\\Users\\siddhant\\Desktop\\Samridh\\Datasets\\PetImages"
categories=["Dog","Cat"]
training_data=[]
def create_training_data():
    for i in categories:
        path=os.path.join(datadir,i)
        class_category=categories.index(i)
        img_size=70
        for img in os.listdir(path):
            try:
                img_array=cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
                new_array=cv2.resize(img_array,(img_size,img_size))
                training_data.append([new_array,class_category])
            except:
                pass
create_training_data()
random.shuffle(training_data)
X=[]
y=[]
for feature,label in training_data:
    X.append(feature)
    y.append(label)
    
X=np.array(X).reshape(-1,img_size,img_size,1)
pickle_out=open("X.pickle","wb")
pickle.dump(X,pickle_out)
pickle_out.close()
pickle_out=open("Y.pickle","wb")
pickle.dump(y,pickle_out)
pickle_out.close()