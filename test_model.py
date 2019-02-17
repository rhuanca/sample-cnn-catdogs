from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K
import numpy as np
import sys


if len(sys.argv) <= 1:
    print("Sample usage: ")
    print("    python3 test_model.py <cat or dot image with jpeg extension>")
    sys.exit(0)

print("image path: %s" % sys.argv[1])

image_path = sys.argv[1]
# dimensions of our images.
img_width, img_height = 150, 150

if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)

model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.load_weights("first_try.h5")

img = image.load_img(image_path, target_size=(img_height, img_width))
y = image.img_to_array(img)
y = np.expand_dims(y, axis=0)

images = np.vstack([y])
classes = model.predict_classes(images, batch_size=10)

print("")
if classes[0][0] == 1:
    print ("it is a dog")
else:
    print ("it is a cat")
