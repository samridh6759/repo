import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout,Conv2D,MaxPooling2D,Flatten,Activation
from tensorflow.keras.callbacks import TensorBoard
import pickle
import time
import time

dense_layers=[0,1,2]
layer_sizes=[32,64,128]
conv_layers=[1,2,3]

pick_in=open('X.pickle','rb')
X=pickle.load(pick_in)
pick_in=open('y.pickle','rb')
y=pickle.load(pick_in)
X=X/255.0

for dense_layer in dense_layers:
	for layers_size in layer_sizes:
		for conv_layer_size in conv_layers: 
			model=Sequential()
			Name="{}-dense-{}-layers-{}-conv-{}".format(dense_layer,layers_size,conv_layer_size,int(time.time()))
			print(Name)
			tensorboard=TensorBoard(log_dir='logs/{}'.format(Name))
			model.add(Conv2D(layers_size,(3,3),input_shape=X.shape[1:]))
			model.add(Activation("relu"))
			model.add(MaxPooling2D(pool_size=(2,2)))

			for l in range(conv_layer_size-1):
				model.add(Conv2D(layers_size,(3,3)))
				model.add(Activation("relu"))
				model.add(MaxPooling2D(pool_size=(2,2)))

			model.add(Flatten())
			for l in range(dense_layer):
				model.add(Dense(layers_size))
				model.add(Activation('relu'))

			model.add(Dense(1))
			model.add(Activation('sigmoid'))

			model.compile(loss="binary_crossentropy",optimizer="Adam",metrics=['accuracy'])

			model.fit(X,y,epochs=5,batch_size=32,validation_split=0.1,callbacks=tensorboard)   # validation_split is the amount of data to be split after each epoch

