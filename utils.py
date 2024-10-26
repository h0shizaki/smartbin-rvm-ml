from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import keras.utils as ku
import numpy as np
from PIL import Image

model = load_model('models/model.h5')
number_to_class = ['cardboard',
                   'glass',
                   'metal',
                   'paper',
                   'plastic',
                   'trash',]

def predict(new_image_path):
    try:
        img = ku.load_img(new_image_path, target_size=(32,32))
        img = ku.img_to_array(img, dtype=np.uint8)
        img = np.array(img)/255.0

        prediction = model.predict(img[np.newaxis, ...])
        print(prediction)
        predicted_value = number_to_class[np.argmax(prediction[0], axis=-1)]
        predicted_accuracy = float(np.max(prediction[0], axis=-1))

        return predicted_value, predicted_accuracy
    except Exception as e:
        return f"Error processing image: {str(e)}", 0