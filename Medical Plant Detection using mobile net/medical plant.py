# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 13:28:30 2023

@author: afsal
"""

from tensorflow.keras.preprocessing import image
from tensorflow import keras
import numpy as np
# testing the model
model = keras.models.load_model('heart.h5')
def testing_image(image_directory):
    test_image = image.load_img(image_directory, target_size = (224, 224))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    test_image = test_image/255
    result = model.predict(x= test_image)
    print(result)
    if np.argmax(result)==0:

       prediction='Dantu'
    elif np.argmax(result)==1:        
       prediction='Jackfruit' 
    elif np.argmax(result)==2:
      prediction='Neem'
    elif np.argmax(result)==3:
      prediction='Basale'
    elif np.argmax(result)==4:
      prediction='Mustard'
    elif np.argmax(result)==5:
      prediction='Lemon'
    elif np.argmax(result)==6:
      prediction='Roxburgh'
    elif np.argmax(result)==7:
      prediction='Peepal'
    elif np.argmax(result)==8:
      prediction='Rosa'
    else:
      prediction='Jasmine'  
    return prediction
print(testing_image(r'AI-S-015.jpg'))